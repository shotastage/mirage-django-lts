import os
import sys
from djconsole.command import log
from djconsole.project import project
from djconsole.flow import Workflow


class DjangoConsoleWorkFlow(Workflow):

    def main(self):
        if project.in_project():
            log("Launching Django Python Shell")
            os.system("python manage.py shell")
        else:
            log("Current dir " + os.getcwd() + " is out of Django project!", withError = True)

        # log("Error Message Test!", withError = True, errorDetail = raise_error_message(parser.add_argument_with_subaction))


class DjangoDBConsoleWorkFlow(Workflow):

    def main(self):
        if project.in_project():
            log("Launching Django Python Shell")
            os.system("python manage.py dbshell")
        else:
            log("Current dir " + os.getcwd() + " is out of Django project!", withError = True)
