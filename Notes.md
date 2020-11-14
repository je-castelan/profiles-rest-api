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