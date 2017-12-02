import os
import readline
from djconsole.generate.urlpy import create_urlpy_script as url_script
from djconsole.console import log, command


def dj_app_flow(third_args):

    try:
        _check_all(third_args)
    except:
        log("Environmental compatability is invalid.", withError = True, withExitOnError = True)
        return


    for app in third_args:
        log("Creating a app " + app + ".")
        _create_app(app)
        _create_url(app)
        _install_app(app)


def _create_app(name):
    command("python manage.py startapp " + name)


def _create_url(name):
    current = os.getcwd()
    os.chdir("./" + name)
    with open("urls.py", "a") as newscript:
        newscript.write(url_script(name))
    os.chdir(current)


"""
Install created app to Django project
"""
def _install_app(name):

    try:
        current = os.getcwd()
    except:
        log("Failed to get current.", withError = True)

    try:
        master_app = __detect_master_app()
    except:
        log("Failed to detect master app.", withError = True)


    log("Installing created app...")
    os.chdir(master_app)

    if os.path.isfile("settings.py"):
        __insert_app_path(name)
    else:
        log("Failed to install Django app due to missing configuration file.", withError = True)

    os.chdir(current)


"""
Check compatibility of Django.
"""
def _check_all(third_args):

    reserved_names = [
        "test",
    ]

    for app in third_args:
        for name in reserved_names:
            if app == name:
                log("The app named " + app + " is reserved by Django!", withError = True)
                raise ValueError

    for app in third_args:
        if os.path.isdir(app):
            log("The app named " + app + " is already exists.", withError = True)
            raise FileExistsError


def __detect_master_app():
    
    try:
        dirs = os.listdir(os.getcwd())
    except:
        log("Failed to detect Django apps.", withError = True)

    current = os.getcwd()

    for app in dirs:

        try:
            os.chdir("./" + app)
            if os.path.isfile("settings.py"):
                log("Master app " + app + " detected.")
                os.chdir(current)
                return app
            else:
                os.chdir(current)
        except:
            pass
       
    return None


def __insert_app_path(app_name):
    lines = []
    insert_line = 0

    try:
        with open("settings.py" , "r") as setting:
            try:
                lines = setting.readlines()
            except:
                log("Failed to load configuration file lines.", withError = True)
    except:
        pass

    
    for i in range(len(lines)):
        if "INSTALLED_APPS = [" in lines[i]:
            insert_line = i
    
    with open("settings.py", "w") as setting:
        app_config = app_name[0].upper() + app_name[1:] + "Config"
        lines.insert(insert_line + 1, "    \'" + app_name + ".apps." + app_config + "\',\n")
        setting.writelines(lines)
