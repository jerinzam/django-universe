================
Django_spider
================

Django_spider is a simple Django app to traverse through your
django code and django file system with ease
Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "django_spider" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'django_spider',
    )

2. Add a variable APPS_FOR_SPIDER  with the app names mentioned like this::
	
    APPS_FOR_SPIDER = [<app name 1>,<app name 2>,<app name 3>, ...]

2. Include the django_spider URLconf in your project urls.py like this::

    url(r'^django_spider/', include('django_spider.urls')),

3. Run `python manage.py migrate` to create the django_spider models.

4. Visit http://127.0.0.1:8000/django_spider/ to start surging through your django code files
