from os import getcwd, chdir, path
from djconsole.console import log, command
from shutil import move
from djconsole.projectstartup.readme import create_readme_doc



def dj_new_flow(name = None):

    if name == None:
        log("Please type your new Django application name.")
        name = log("Django project name", withInput = True)

    try:
        __check(name)
    except:
        log("Project {0} is already exists.".format(name), withError = True)
        return


    _create_new_django_app(name)

    current = getcwd()
    chdir("./" + name)
    _create_template_git_project(name)
    _create_docs(name)
    chdir("../")


def _create_new_django_app(name):
    command("django-admin startproject " + name)


def _create_template_git_project(name):
    command("curl -O https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore")
    move("Python.gitignore", ".gitignore")
    command("git init")

def _create_docs(name):
    with open("README.md", "a") as readme:
        readme.write(create_readme_doc(name))


def __check(name):
    if path.exists(name):
        raise FileExistsError
