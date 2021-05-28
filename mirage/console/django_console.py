import os

from mirage import proj
from mirage import system as mys
from mirage.flow import Workflow


class DjangoConsoleWorkFlow(Workflow):

    def main(self):
        with proj.MirageEnvironment(proj.MirageEnvironmentLevel.indjango):
            mys.log("Launching Django Python Shell")
            os.system("python manage.py shell")


class DjangoDBConsoleWorkFlow(Workflow):

    def main(self):
        with proj.MirageEnvironment(proj.MirageEnvironmentLevel.indjango):
            mys.log("Launching Django Python Shell")
            os.system("python manage.py dbshell")
