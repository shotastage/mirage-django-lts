from djconsole.flow import Flow

from os import getcwd, chdir, path
from djconsole.command import log, command
from shutil import move
from djconsole.projectstartup.readme import create_readme_doc



class DjangoStartupFlow(Flow):

    def __init__(self, name = None):
        self._project_name = name

    def flow(self):

        if self._project_name == None:
            log("Please type your new Django application name.")
            self._project_name = log("Django project name", withInput = True)

        try:
            self._check(self._project_name)
        except:
            log("Project {0} is already exists.".format(self._project_name), withError = True)

        
        self._create_new_django_app(self._project_name)

        current = getcwd()
        chdir("./" + self._project_name)
        self._create_template_git_project(self._project_name)
        self._create_docs(self._project_name)
        chdir("../")


    def _create_new_django_app(self, name):
        command("django-admin startproject " + name)


    def _create_template_git_project(self, name):
        command("curl -O https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore")
        move("Python.gitignore", ".gitignore")
        command("git init")

    def _create_docs(self, name):
        with open("README.md", "a") as readme:
            readme.write(create_readme_doc(name))


    def _check(self, name):
        if path.exists(name):
            raise FileExistsError
