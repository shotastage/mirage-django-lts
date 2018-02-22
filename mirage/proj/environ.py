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
import pathlib
from mirage import proj
from mirage import fileable
from mirage.command import log


class MirageEvironmet():
    
    def __init__(self, env_level):
        log("Enter Mirage Environ")
        self._level = env_level

    def __enter__(self):

        proj_root = MirageEvironmet.search_project_root()

        with proj.InDir(proj_root):
            if self._level == MirageEvironmetLevel.inproject:
                os.chdir()

    def __exit__(self, exception_type, exception_value, traceback):
        return False



    @staticmethod
    def search_project_root():
        """
        Search your Django project root.

        returns:
            - path:string  Django project root
        """

        while True:

            current = os.getcwd()
            
            if pathlib.Path("Miragefile").is_file():
                return current
            else:
                os.chdir("../")


    @staticmethod
    def set_import_root():
        sys.path.append("./")


    @staticmethod
    def in_project():
        try:
            MirageEvironmet.set_import_root()
            import manage
            return True
        except ImportError:
            return False
        except:
            return False


    @staticmethod
    def in_app():
        try:
            MirageEvironmet.set_import_root()
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

        if not MirageEvironmet.in_project(): return

        for dir_file in list_dir:
            if os.path.isdir(dir_file):
                os.chdir(dir_file)
                if MirageEvironmet.in_app():
                    apps.append(dir_file)
                os.chdir(current)
            else:
                continue

        return apps



class MirageEvironmetLevel(enum.Enum):
    inproject   = 0
    inapp       = 1
    outproject  = 2




def get_project_name():
    current_dir = os.getcwd()
    directories = os.listdir(".")
    app_name = "FAILED TO GET"
    
    if MirageEvironmet.in_project():

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
