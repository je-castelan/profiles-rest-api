Notes
=====

# Licence
Recommended to add licence on [this page](https://choosealicense.com/licenses/mit/).

# Git ignore
We need not to load some files to Github. The prefered gitignore for Python project can be downloaded on [this page](https://gist.github.com/LondonAppDev/dd166e24f69db4404102161df02a63ff).

# Vagrant project

We need to use the following command to create a Vagrant virtual environment

> vagrant init ubuntu/bionic64

For this Django project, we can use this [vagrantfile](https://gist.github.com/LondonAppDev/199eef145a21587ea866b69d40d28682)

For running our virtual environment, we use `up`

> vagrant up

To connect via ssh to our project

> vagrant ssh

Execution project is here

> cd /vagrant

And finnaly, to shutdown it

> vagrant halt

# Remembering Python and Django basics

Virtual environment

> python -m venv ~/venv

Activate environment

>  source ~/venv/bin/activate

Deactivate environment

> deactivate

Install requirement packages. Last versions are [here](https://pypi.org/)

> pip install -r requirements.txt 

Create new django project (the point allows us to have project and apps on root).

> django-admin.py startproject profiles_project .

Create app

> python manage.py startapp profiles_api

Add apps to your project. Enter to [project] -> settings.py and add the app

```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    '[APP]',
]
```

Run project

> python manage.py runserver 0.0.0.0:8000

Create migration files models

> python manage.py makemigrations

Create migration files models for a specific app

> python manage.py makemigrations APP_NAME

Create superuser for Django admin

> python manage.py createsuperuser

Migrate models

> python manage.py migrate

# User model
You can check the model [here](profiles_api/models.py).

Usualy we use "User model" on `django.contrib.auth.models` but in orde. to customize our own usermodel (for example, login with email), we need to use "AbstractBaseUser model", and "PermissionsMixin" to customize permissions like staff.

We need to specify the field which allow us to login with the system with the parameter `USERNAME_FIELD`.

The parameter `REQUIRED_FIELDS` notifies the required fields to fill with a new user.

Remember to create a `__str__` function to mark us a name for the object which use this class.

The class use another class as manager which imports from `BaseUserManager`. With this class, we can create management functions to new users. It is important to create it because the default commands are only available on user default model.

It is highly recommended to normalize emails with `self.normalize_email()` in order to switch to lowercase the provided emails.

The function `self.model(**args)`allows us to create the object. For this, it is neccesary than the AbstractUserBase has declared a objects asociated to this class (using `objects = UserProfileManager()`)

Other used function is `self.set_password(password)` which encripts the inserted password to a hash.

The user has a attribute `superuser` which can manage to the database (it is independent to other manager paramentes like "staff").

Finally, we need to save it (using `user.save()`). It is recommended to use the parameter `using` for future multiple databases.

On [settings file](profiles_project/settings.py) we need to specify the model to autenticate with the parameter `AUTH_USER_MODEL`.

# Django admin
You can check the model [here](profiles_api/admin.py).

On APP we need to have `admin` class imported from `django.contrib` and import the model class.

We assign a admin manager with `admin.site.register(path.class)`

# API Views

## Introduction

Django REST Frameworks offers the following 2 kind of classes

 - APIView
 - ViewSet

In this case, we will work with `APIView` as the easier way to describe logic to make API endpoints.

An APIView allow to define HTTP standard methods for functions. The basic methods are.

 - GET: Get one or more items
 - POST: Create an item
 - PUT:  Update an item
 - PATCH: Partially update an item
 - DELETE: Delete an item

 APIviews give us most control over the logic. Its perfect to implement complex logic as calling  other API's and controlling files.

 We can use APIViews as we prefer based on our experience. It's recommended to use when we need full control over the logic, and required to process files and rendering a syncronous response. Also when you need to call other API's or services and access to local files or data.

## Create my first APIview
You can check the view [here](profiles_api/views.py).

 To create an APIView, we need to update the views file and import `APIView` form `rest_framework.views` and `Response` from `rest_framework.response`.

 The class will be inherit from `APIView`. In the new class, we define the allowed functions (get, post, etc). Remember to require `self` and `request` on the functions. Also it's best practice to define a format, although it could be None.

 The function returns a Response object with a dict with the values than front end requires.

 ## Configure URL views
 Check general url's [here](profiles_project/urls.py) and app url [here](profiles_project/api.py).

On URL project we can import all the URLs of the api inserting other element on the urlpatterns list. For this, we need to add a `path` and an `include` (import from `django url`). The element is and include object with the required parameters.
 - Prefix assigned to app
 - include object the the url file of the app (app.urls)

On URL app we need to import path (`django_urls`) and the app's views. The we create a particular list called urlpatterns. It will have a path object with
 - Name of page
 - View function of the page with the funcion `as_view()`

You will access to the funtions inserting 

> HOST/PREFIX_APP/VIEW_PAGE

## Serializers
You can check serializers [here](profiles_api/serializers.py).  Also, you can check post function [here](profiles_api/views.py).

It allows to convert input values to Python objects and viceversa.

It requires from `rest_framework` the class `serializers`. New serializer classes with inherit from `serializers.Serializer`.

The new class with have name of fields (like Django forms) using serializers instead of forms.

To use it on a View, we need to declare it as an attribute of our view class as `serializer_class`.

The function which use it, we need to use an object using `serializer_class` inserting the parameter `data=rquest.data`. It convert the data request to serializer object with the data on the request.

The best practice it work with a serializer with valid values. So we can use `is_valid()` function to works only if the serializers values are valid. Also, we can get the serializer valid values using `serializer.validated_data.get()`.


## Status

Status object allows to notify user the result of the action (404 NOT FOUND, 200 OK). It cames on `status` from `rest_framework`.

You can add an error on Response object on the return inserting as a parameter `serializer.error, status = status.HTTP_400_BAD_REQUEST` (you can find status [here](https://www.django-rest-framework.org/api-guide/status-codes/))

If a function drops this error, it will mark the field and the error committed.

# ViewSet

## Introduction

It manage the THHP actions with the following functions:

 - List: As GET
 - Create: As POST
 - Retrieve: Getting a specific object (GET)
 - Update: like PUT
 - Partial_update: Like PATCH
 - Destroy: Like DELETE

 Viewsets takes care of a lot of typical logic for you because it has precharged standard database operations. It allows to have a fastest way to make a database interface.

 It recomends to use ViewSet in case to create a simple CRUD, a simple API or make a not complex logic. It works with standard data structures

 ## Create first ViewSet
 You can check the view [here](profiles_api/views.py).

It requires to import `viewsets` from `rest_framework`. New class must inherit from `viewsets.ViewSet`.

## URL Router
Check general url's [here](profiles_api/urls.py)

To point a ViewSet with URL, we need to create a Router.

On urls file, we need to import `DefaultRouter` from `rest_framework.routers`.

We need to create an object from DefaultRouter and execute the function `register` with the following parameters

 - Prefix of the APIView assigned
 - ViewSet class created on views
 - Base name to know it on web pages

 On urlpatterns object, we need to add a path with the following elements:
  - Black first for prefix (we assigned on the defaultrouter)
  - Include object pointing to attribute `urls` to the router object

Viewset is accesible with the following path

> URL_SERVER/api/APIVIEW_PREFIX

URL's on a app take priority to ViewSet (it's probably than you doesn't find at first look the APIView)

## Serializers

We still using serializers to validate values declaring the class used as class attibute `serializer_class`. On the functions, we associate values with ` self.serializer_class(data=request.data)`

## Testing

In order to test, we need to set at the final of the URL any value than represents the object id to PUT, PATCH or DELETE.