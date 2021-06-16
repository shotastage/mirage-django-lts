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

from mirage.flow import Flow
from mirage.generate.urlpy import create_urlpy_script as url_script
from mirage.command import log, command



class DjangoSerializerMakeFlow(Flow):

    def __init__(self, serializer):
        self._must_creat_serializer = serializer


    def flow(self):
        try:
            self._check_all()
        except:
            log("Environmental compatability is invalid.", withError = True)
            return


        for app in self._must_creat_serializer:
            log("Creating a selia " + app + ".")
            self._create_app(app)
            self._create_url(app)
            self._install_app(app)


    def _create_app(self, name):
        command("python manage.py startapp " + name)


    def _create_url(self, name):
        current = os.getcwd()
        os.chdir("./" + name)
        with open("urls.py", "a") as newscript:
            newscript.write(url_script(name))
        os.chdir(current)


    """
    Install created app to Django project
    """
    def _install_app(self, name):

        try:
            current = os.getcwd()
        except:
            log("Failed to get current.", withError = True)

        try:
            master_app = self.__detect_master_app()
        except:
            log("Failed to detect master app.", withError = True)


        log("Installing created app...")
        os.chdir(master_app)

        if os.path.isfile("settings.py"):
            self.__insert_app_path(name)
        else:
            log("Failed to install Django app due to missing configuration file.", withError = True)

        os.chdir(current)


    """
    Check compatibility of Django.
    """
    def _check_all(self):

        reserved_names = [
            "test",
        ]

        for app in self._must_creat_serializer:
            for name in reserved_names:
                if app == name:
                    log("The app named " + app + " is reserved by Django!", withError = True)
                    raise ValueError

        for app in self._must_creat_serializer:
            if os.path.isdir(app):
                log("The app named " + app + " is already exists.", withError = True)
                raise FileExistsError


    def __detect_master_app(self):
        
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


    def __insert_app_path(self, app_name):
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
