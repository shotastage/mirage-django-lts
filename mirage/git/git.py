from mirage.flow import Workflow
from mirage import system as mys


class DjangoGitPullFlow(Workflow):

    def main(self):
        mys.command("git pull origin main")


class DjangoGitPushFlow(Workflow):

    def main(self):
        commit_message = mys.log("Commit message: ", withInput = True, default = "update code base")
        mys.command("git add .")
        mys.command("git commit -m \"" + commit_message + "\"")
        mys.command("git push -u origin main")
