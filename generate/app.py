import os
from generate.urlpy import create_urlpy_script as url_script
from console import log, command


def dj_app_flow(third_args):

    if not _check_all(third_args):
        log("Environmental compatability is invalid.", withError = True, withExitOnError = True)

    for app in third_args:
        log("Creating a app " + app + ".")
        _create_app(app)
        _create_url(app)


def _create_app(name):
    command("python manage.py startapp " + name)

def _create_url(name):
    current = os.getcwd()
    os.chdir("./" + name)
    with open("urls.py", "a") as newscript:
        newscript.write(url_script(name))
    os.chdir(current)


def _check_all(third_args):
    status = True

    for app in third_args:
        if os.path.isdir(app):
            log("The app named " + app + " is already exists.", withError = True)
            status = False
    return status
