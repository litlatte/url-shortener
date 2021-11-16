## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Local Setup](#local-setup)

## General info
This is url shortener that allows you to link a slug to url.

Unauthenticated users are not allowed to choose the slug, while authenticated user are allowed to do it.
Authenticated user can also see the number of clicks of a certain slug and see who clicked it.
For every click ip address, timestamp and user (if authenticated) are stored and avaible on the click page of the slug.
slugs and clicks pages are avaible only for authenticated users.
	
## Technologies
Project is created with
* Django 3.2.4
* Python 3.7

## Local Setup
The first step is to irst thing is to install the required libraries by doing:
`python -m pip install -r requirements.txt`

The normal process for setting up a django project would continue by doing:
```
python manage.py makemigrations app1 app2 app3
python manage.py migrate
```
where app1 app2 app3 are the names of our applications but since this project has a circular dependency we have to  do some steps before.

The first thing to do is to go to the `./users/models.py` file and comment the line number 13 and save the file like this:
```python
 class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'),unique=True)
    #slugs = models.ManyToManyField('redurl.RedUrl', related_name='slugs',blank=True )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
```
The second step is to run the two migration commands:
```
python manage.py makemigrations users redurl
python manage.py migrate
```
at this point we uncomment the line 13 from `./users/models.py` in this way:
```python
 class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'),unique=True)
    slugs = models.ManyToManyField('redurl.RedUrl', related_name='slugs',blank=True )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
```
and now we run:
```
python manage.py makemigrations users
python manage.py migrate
```

Finally to start our server we run:
```
python manage.py runserver
```