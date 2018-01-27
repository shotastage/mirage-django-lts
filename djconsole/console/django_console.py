import os
from djconsole.command import log
from djconsole.flow import Flow, Workflow


class DjangoConsoleWorkFlow(Workflow):

    def main(self):
        log("Launching Django Python Shell")
        os.system("python manage.py shell")


class DjangoDBConsoleWorkFlow(Workflow):

    def main(self):
        log("Launching Django Python Shell")
        os.system("python manage.py dbshell")
