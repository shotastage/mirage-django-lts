import os

from djconsole.flow import Flow
from djconsole.command import log
from djconsole.command import command


class DjangoGitFlow(Flow):

    def __init__(self, subcommand):
        log("Django Console Git is now unser development!", withError = True)
        self._subcommand = subcommand

    def flow(self):
        os.system("git " + self._subcommand)

    def _pull(self):
        command("git pull origin master")

    def _puash(self):
        command("git push -u origin master")
