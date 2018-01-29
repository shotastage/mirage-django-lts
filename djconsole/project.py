import os
from djconsole.command import log



# New
import sys

def in_project():
    try:
        set_import_root()

        import manage

        return True
    except ImportError:
        return False

def in_app():
    set_import_root()

def set_import_root():
    sys.path.append("./")




# Old
def isproject():
    if os.path.isfile("manage.py"):
        return True
    else:
        return False

def project_name():
    if isproject:

        contents = os.listdir(os.getcwd())

        for test in contents:
            if os.path.isdir(test):
                current = os.getcwd()
                os.chdir(test)
                if os.path.isfile("settings.py"):
                    return str(test)
                os.chdir(current)
