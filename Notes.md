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
