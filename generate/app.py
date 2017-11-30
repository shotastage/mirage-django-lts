import os
from console import log


def dj_app_flow(third_args):

    if not _check_all(third_args):
        log("Environmental compatability is invalid.", withError = True, withExitOnError = True)

    for app in third_args:
        log("Creating a app " + app + ".")

def _check_all(third_args):
    status = True

    for app in third_args:
        if os.path.isdir(app):
            log("The app named " + app + " is already exists.", withError = True)
            status = False
    return status
