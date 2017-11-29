from os import system
from console import log

def dj_new_flow(name = None):
    _create_new_django_app(name)
    _create_template_git_project()

def _create_new_django_app(name):
    log("Please type your new Django application name.")

    if not name == None:
        system("django-admin startproject " + name)
    else:
        name = log("App Name", withInput = True)
        system("django-admin startproject " + name)

def _create_template_git_project():
    pass
