from console import command
from os import chdir
from shutil import move
from console import log

def dj_new_flow(name = None):
    if name == None:
        log("Please type your new Django application name.")
        name = log("App Name", withInput = True)
    _create_new_django_app(name)
    _create_template_git_project(name)


def _create_new_django_app(name):
    command("django-admin startproject " + name)


def _create_template_git_project(name):
    chdir("./" + name)
    command("curl -O https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore")
    move("Python.gitignore", ".gitignore")
