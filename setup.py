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
    license='MIT',
    install_requires=[
        'Django>=1.6',
    ]
)
