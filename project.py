from os import system
from console import log

def dj_new_flow():
    _create_new_django_app()
    _create_template_git_project()

def _create_new_django_app():
    log("Please type your new Django application name.")

    name = log("App Name", withInput = True)
    system("django-admin startproject " + name)

def _create_template_git_project():
    pass
