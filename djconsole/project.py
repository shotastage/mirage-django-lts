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
from djconsole         import fileable
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
    except:
        return False


def in_app():
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
    sys.path.append("./")



def get_project_name():
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

    apps = []
    list_dir = os.listdir(os.getcwd())
    current = os.getcwd()

    if not in_project:
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
def isproject():
    warnings.warn(
            "project.isproject will be depricated on next version!",
            PendingDeprecationWarning)
    
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


# Config

def load_djfile():
    with open("DjFile", "r") as djfile:
        try:
            return yaml.load(djfile)
        except:
            raise Exception
