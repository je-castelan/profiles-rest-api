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

And finnaly, to shutdown it

> vagrant halt

