import os
import sys

from djconsole import project
from djconsole.command import log
from djconsole.flow import Workflow


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
