import os

from mirage.flow import Flow
from mirage.command import log
from mirage.command import command
from mirage import system as mys


class DjangoGitPullFlow(Flow):

    def __init__(self, subcommand):
        log("Django Console Git is now unser development!", withError = True)

    def flow(self):
        command("git pull origin main")


class DjangoGitPushFlow(Flow):

    def __init__(self, subcommand):
        log("Django Console Git is now unser development!", withError = True)

    def flow(self):
        commit_message = mys.log("Commit message: ", withInput = True, default = "update code base")
        command("git add .")
        command("git commit -m " + commit_message)
        command("git push -u origin main")
