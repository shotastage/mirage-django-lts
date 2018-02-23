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
from mirage.miragefile import conf
from mirage.command import log


class MirageEvironmet():
    
    def __init__(self, env_level):
        self._current = os.getcwd()
        self._level = env_level

    def __enter__(self):

        if self._level == MirageEvironmetLevel.inproject:
            proj_root = MirageEvironmet.search_project_root()
            os.chdir(proj_root)
            return
        
        if self._level == MirageEvironmetLevel.indjango:
            django_root = conf.Config().get(conf.Category.django, conf.Detail.django_path)
            os.chdir(django_root)
            return

        if self._level == MirageEvironmetLevel.inapp:
            app_root = MirageEvironmet.search_app_root()
            os.chdir(app_root)
            return

        
    def __exit__(self, exception_type, exception_value, traceback):
        os.chdir(self._current)



    @staticmethod
    def search_project_root():
        """
        Search your Django project root.

        returns:
            - path:string  Django project root path
        """

        while True:

            current = os.getcwd()
            
            if pathlib.Path("Miragefile").is_file():
                return current
            else:
                os.chdir("../")

    @staticmethod
    def search_app_root():
        """
        Search your Django application root

        returns:
            - (String) Django application root path
        """
        while True:

            current = os.getcwd()
            
            if pathlib.Path("app.py").is_file():
                return current
            else:
                os.chdir("../")


    @staticmethod
    def set_import_root():
        """
        Set path to import current dir Python module.
        """
        sys.path.append("./")


    @staticmethod
    def in_project():
        """
        Judge where current working directory is in Django project or not.

        returns:
            - (Bool) cwd is in proj dir returns True
        """
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
        """
        Judge where current working directory is in Django application or not.

        returns:
            - (Bool) cwd is in app dir returns True
        """
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
        """
        Return application lists.

        returns:
            - (Array<String>) cwd is in app dir returns True
        """

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
    indjango    = 1
    inapp       = 2
    outproject  = 3




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
