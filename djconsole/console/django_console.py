import os
from djconsole.command import log
from djconsole.flow import Flow


class DjangoConsoleFlow(Flow):

    def flow(self):
        log("Launching Django Python Shell")
        os.system("python manage.py shell")


class DjangoDBConsoleFlow(Flow):

    def flow(self):
        log("Launching Django Python Shell")
        os.system("python manage.py dbshell")
