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
import sys
import enum
from mirage import fileable
from mirage.command import log


class MirageEnvironment():
    
    def __init__(self, env_level):
        log("Enter Mirage Environ")
        self._level = env_level

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        return False

    def __del__(self):
        log("Out Mirage Environ")


    @staticmethod
    def set_import_root():
        sys.path.append("./")


    @staticmethod
    def in_project():
        try:
            MirageEnvironment.set_import_root()
            import manage
            return True
        except ImportError:
            return False
        except:
            return False


    @staticmethod
    def in_app():
        try:
            MirageEnvironment.set_import_root()
            import apps
            if os.path.isfile("apps.py"):
                return True
            else:
                return False
        except ImportError:
            return False
        except:
            return False


    @staticmethod
    def get_app_list():

        apps = []
        list_dir = os.listdir(os.getcwd())
        current = os.getcwd()

        if not MirageEnvironment.in_project(): return

        for dir_file in list_dir:
            if os.path.isdir(dir_file):
                os.chdir(dir_file)
                if MirageEnvironment.in_app():
                    apps.append(dir_file)
                os.chdir(current)
            else:
                continue

        return apps



class MirageEnvironmentLevel(enum.Enum):
    inproject   = 0
    inapp       = 1
    outproject  = 2




def get_project_name():
    current_dir = os.getcwd()
    directories = os.listdir(".")
    app_name = "FAILED TO GET"
    
    if MirageEnvironment.in_project():

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
