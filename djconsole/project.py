from os import path, listdir, chdir
import os
from djconsole.command import log


def isproject():
    if path.isfile("manage.py"):
        return True
    else:
        return False

def project_name():
    if isproject:

        contents = listdir(os.getcwd())

        for test in contents:
            if path.isdir(test):
                current = os.getcwd()
                chdir(test)
                if os.path.isfile("settings.py"):
                    return str(test)
                os.chdir(current)
