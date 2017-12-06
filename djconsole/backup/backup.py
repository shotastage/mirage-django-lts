import os
import shutil
from djconsole.command import log
from djconsole import project
from djconsole.flow import Flow

class DjangoBackupFlow(Flow):

    def flow(self):
        pass
    


def create_buckup_dir():
    if project.isproject:
        if not os.path.isdir(".djc/backup/"):
            try:
                os.makedirs(".djc/backup/")
            except:
                log("Failed to prepare .djc/backup with unknown error.", withError = True)
