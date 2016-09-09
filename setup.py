import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='django_universe',
    version='0.1',
    packages=['django_universe'],
    description='A line of description',
    long_description=README,
    author='jerin',
    author_email='jerinzam@gmail.com',
    url='https://github.com/jerinzam/django-universe/',
    download_url='https://github.com/jerinzam/django-universe/dist/django_universe-0.1.tar.gz',
    license='MIT',
    install_requires=[
        'Django>=1.6',
    ]
)
