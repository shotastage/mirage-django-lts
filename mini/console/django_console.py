import os
import sys

from mirage import project
from mirage import system as mys
from mirage.flow import Workflow


class DjangoConsoleWorkFlow(Workflow):

    def main(self):
        if project.in_project():
            mys.log("Launching Django Python Shell")
            os.system("python manage.py shell")
        else:
            mys.log("Current dir " + os.getcwd() + " is out of Django project!", withError = True)


class DjangoDBConsoleWorkFlow(Workflow):

    def main(self):
        if project.in_project():
            mys.log("Launching Django Python Shell")
            os.system("python manage.py dbshell")
        else:
            mys.log("Current dir " + os.getcwd() + " is out of Django project!", withError = True)
