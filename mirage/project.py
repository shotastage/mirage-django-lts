# -*- coding: utf-8 -*-
"""
Copyright 2017-2018 Shota Shimazu.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import os
import json
import sys
from mirage.system import warning

def in_project():
    warning.warn("mirage.project is now pending deprecation.", warning.PendingDeprecationWarning)
    try:
        set_import_root()

        import manage

        return True
    except ImportError:
        return False
    except:
        return False


def in_app():
    warning.warn("mirage.project is now pending deprecation.", warning.PendingDeprecationWarning)
    try:
        set_import_root()

        import apps
        
        if os.path.isfile("apps.py"):
            return True
        else:
            return False
    except ImportError:
        return False
    except:
        return False


def set_import_root():
    warning.warn("mirage.project is now pending deprecation.", warning.PendingDeprecationWarning)
    sys.path.append("./")



def get_project_name():
    warning.warn("mirage.project is now pending deprecation.", warning.PendingDeprecationWarning)
    current_dir = os.getcwd()
    directories = os.listdir(".")
    app_name = "FAILED TO GET"
    
    if in_project():

        for directory in directories:
            try:
                os.chdir(directory)

                if os.path.isfile("settings.py"):
                    app_name = str(os.getcwd()).split("/")[-1]

                os.chdir(current_dir)
            except:
                pass
    else:
        app_name = "Out of project dir"
    
    return app_name



def get_app_list():
    warning.warn("mirage.project is now pending deprecation.", warning.PendingDeprecationWarning)
    
    apps = []
    list_dir = os.listdir(os.getcwd())
    current = os.getcwd()

    if not in_project():
        return

    for dir_file in list_dir:
        if os.path.isdir(dir_file):
            os.chdir(dir_file)
            if in_app():
                apps.append(dir_file)
            os.chdir(current)
        else:
            continue

    return apps


# Old
def project_name():
    warning.warn("mirage.project is now pending deprecation.", warning.PendingDeprecationWarning)
    
    status = False

    if os.path.isfile("manage.py"):
        status = True
    else:
        status = False

    if status:

        contents = os.listdir(os.getcwd())

        for test in contents:
            if os.path.isdir(test):
                current = os.getcwd()
                os.chdir(test)
                if os.path.isfile("settings.py"):
                    return str(test)
                os.chdir(current)


# Config

def load_djfile():
    warning.warn("mirage.project is now pending deprecation.", warning.PendingDeprecationWarning)
    
    with open("Miragefile", "r") as djfile:
        try:
            return json.load(djfile)
        except:
            raise Exception


def load_additional_conf():
    warning.warn("mirage.project is now pending deprecation.", warning.PendingDeprecationWarning)
    
    with open("Miragefile.addon", "r") as djfile:
        try:
            return json.load(djfile)
        except:
            raise Exception


def load_secret_conf():
    warning.warn("mirage.project is now pending deprecation.", warning.PendingDeprecationWarning)

    with open("Miragefile.secret", "r") as djfile:
        try:
            return json.load(djfile)
        except:
            raise Exception
