import os
import sys

from mirage import project
from mirage.command import log
from mirage.flow import Workflow


class DjangoConsoleWorkFlow(Workflow):

    def main(self):
        if project.in_project():
            log("Launching Django Python Shell")
            os.system("python manage.py shell")
        else:
            log("Current dir " + os.getcwd() + " is out of Django project!", withError = True)


class DjangoDBConsoleWorkFlow(Workflow):

    def main(self):
        if project.in_project():
            log("Launching Django Python Shell")
            os.system("python manage.py dbshell")
        else:
            log("Current dir " + os.getcwd() + " is out of Django project!", withError = True)
