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

# Profiles API

## Model Serializer
We use it in cse to validate values for a model object. This is a class inherited from `serializers.ModelSerializer`.

To initialize this class, we need to create an internal class called `Meta`. Into this subclass we can define the following:
 - `model` = The model connected to this serializer.
 - `fields` =  field to manage on the serializer on the model. It's neecesary to declare it in a list
 - `extra_kwags` = A dictionary which we can adjust caracteristics to the fields on the serializer. For example, it a field is read only and if it is neccesary to use a kind of input type on the browsable api to charge it.

```
extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
```

We can overrde `create` function in order to do extra actions (in the case of user model, we need to adjust the password as a hash and use the "create user" function which encript it). When we configure this function, it is neccesary to use the validated values (example `field = validated_data['field']`)

## ModelViewSet

It works like ViewSet but works indicating a model to work (and indicting a specific query to manage the objects).

It must be inherit from `viewsets.ModelViewSet` and we can configurate the following attributes:
 - serializer_class which validates the information
 - queryset to manage required objects.

Remember to connect it with a router to url files. When we test it, we can use the GET, POST, PUT, PATCH nad DELETE options

## Permissions
You can check the view [here](profiles_api/permissions.py).

We ned to import `permissions` from `rest_framework`. The permission class must inherit from `permissions.BasePermission`.

To manage permissions to execute a HTTP method, we need to create the function `has_object_permission(self, request, view, obj)`.

In the next example, the permission class will check than the owner user is making the method. If not, it can only execute safeful methods (like GET).

```
class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # If method is safeful (GET)
        if request.method in permissions.SAFE_METHODS:
            return True
        # If not safeful, it must check if the method is executed by the same user.
        return obj.id == request.user.id
```

To assign this permission class, we need to assign the attibute `permission_classes` on the ViewSet. This attribute must be a tuple (example: `permission_classes = (permissions.UpdateOwnProfile,)`)

## Tokens

In case than you are using permission class to check authenticated users, you will need the token authentication method than Django is usign. So, on the view set you must assign the attribute `authentication_classes` with a tuple which contains the class `TokenAuthentication` (for example: `authentication_classes = (TokenAuthentication,)`). This class is imported from `rest_framework.authentication`.

## Searching

You can assign other fields (apart of id) to search registers on the viewset.

 - It required to import `filter` from `rest_framework`
 - On viewset, we need to assign the attribute `filter_backends` with a tuple which must contain the value `filters.SearchFilter`
 - On viewset also we need to assign the attribute `search_fields` with a tuple which will have the search fields (example `search_fields = ('name', 'email',)`)


 You could execute GET requirements with the following sintaxis to execute search.

> SERVER:PORT/APP_PREFIX/VIEWSET_PREFIX/?search=value

# Login

## Login API Viewset
We can create a Viewset to manage the login API page.
In this case, we can use default resources to manage the login with tokens. For this, we need to import `ObtainAuthToken` from `rest_framework.authtoken.views`.
We need to create a new class which inherit from `ObtainAuthToken`. It must have the attibute `renderer_classes` equals to `api_settings.DEFAULT_RENDERER_CLASSES` (it's neccesary to import `api_settings` from `rest_framework.settings`).

Finally, it's neccesary to add on the url.py file the viwset on the router object.

It's neccesary to access login page as POST method. When you ingress your email and password, POST method will return a JSPON with a token value. This token refers the user which logged on future requirements. It must be assigned on the HTTP request.

## Using ModHeader extension

To add the token on HTTP request, we can open ModHeader and add the following parameter:
 - Authentication. The value is "Token x" . x is the token obtained on login.


# Miscelaneous

## Using user model in other classes

When you want to use the user model in other classes (example: foreign key), it is best practice to point to the `AUTH_USER_MODEL` variable on settings.py file (`import django.conf import settings`)

## Perform create, update and delete

It's possible than a viewset, you need to make any aditiona action before to create, update and delete. On the view set, you can override the functions `perform_create`, `perform_update` and `perform_delete`. If you want more detail, you can check it [here](https://www.django-rest-framework.org/api-guide/generic-views/).

## IsAuthenticatedOrReadOnly y IsAuthenticated

Both classes are imported from `rest_framework.permissions`. 

 - `IsAuthenticatedOrReadOnly`: This class define if there is a logged user. Otherwise, it will show the APIVies as readonly.
 - `IsAuthenticated`: This class define if there is a logged user. Otherwise, it will not show the APIView

 # Deploy on AWS

We can upload our API on a AWS Free Tier [here](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc).
 
## Public key

We upload the content of the ssh public key (`cat ~/.ssh/id_rsa.pub`) on the section Sevices -> Compute/EC2. Then search Network & Security / Key Pairs.

We will select the "Import key pair" action and paste the public key.

## EC2 server instance

On the section Sevices -> Compute/EC2, then select `Launch instance`.

In order to follow the Ubuntu version, we need to search `Ubuntu Server 18.04 LTS (HVM), SSD Volume Type` instance and check than it works as `Free tier eligible`.

Then, oninstance type, we need to check which type is `free tier elegble`.

On Configure Instance Details steps, we look on `6: Configure Security Group` to add http service.

When we launch the server, check your own key pair 

## Scripts and changes required

On [this folder](deploy) we will find the following information.

 - `setup.sh`: Script to install all the required dependences for the project. We need to insert the project's github https location.
 - `supervisor_profiles_api.conf`: Supervisor controller with environment variables.
 - `nginx_profiles_api.conf`: NGINX configuration to serve static files.
 - `update.sh`: Check any new change on github and reload it

Scripts must change the priviledges with `chmod +x deploy/*sh`

On `settings.py` :

 - Change DEBUG to False. Due than `supervisor_profiles_api.conf` has debug variable as false, we can set `DEBUG = bool(int(os.environ.get('DEBUG', 1)))
 - STATIC_ROOT = `static/`
 - ALLOWED_HOSTS = ['[Public IPV4 DNS]','127.0.0.1']

## Deployment

On the section Sevices -> Compute/EC2, then select `Running instances`. Then, select the server and get the `Public IPv4 DNS` URL and access it from your allowed PC via ssh with `ubuntu` user.

Then, execute `curl -sL [setup.sh file on github url] | sudo bash -`