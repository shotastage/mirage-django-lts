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
import yaml
import warnings
from mirage         import fileable
from mirage.command import log


# New
import sys

def in_project():
    warnings.warn("in_project will be deprecated on next release.", PendingDeprecationWarning)
    try:
        set_import_root()

        import manage

        return True
    except ImportError:
        return False
    except:
        return False


def in_app():
    warnings.warn("in_app will be deprecated on next release.", PendingDeprecationWarning)
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
    warnings.warn("set_import_root will be deprecated on next release.", PendingDeprecationWarning)
    sys.path.append("./")



def get_project_name():
    warnings.warn("get_project_name will be deprecated on next release.", PendingDeprecationWarning)
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
    warnings.warn("get_app_list will be deprecated on next release.", PendingDeprecationWarning)

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
    warnings.warn("project_name will be deprecated on next release.", PendingDeprecationWarning)

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
    warnings.warn("load_djfile will be deprecated on next release.", PendingDeprecationWarning)

    with open("Miragefile", "r") as djfile:
        try:
            return yaml.load(djfile)
        except:
            raise Exception


def load_additional_conf():
    warnings.warn("load_additional_conf will be deprecated on next release.", PendingDeprecationWarning)

    with open("Miragefile.addon", "r") as djfile:
        try:
            return yaml.load(djfile)
        except:
            raise Exception


def load_secret_conf():
    warnings.warn("load_secret_conf will be deprecated on next release.", PendingDeprecationWarning)

    with open("Miragefile.secret", "r") as djfile:
        try:
            return yaml.load(djfile)
        except:
            raise Exception
