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
from mirage.core import Void
from mirage.flow import Workflow
from mirage.generate.urlpy import create_urlpy_script as url_script
from mirage import system as mys
from mirage import proj



class DjangoAppMakeWorkFlow(Workflow):

    def constructor(self) -> Void:
        self._must_creat_apps = self._values


    def main(self) -> bool:
        try:
            self._check_all()
        except:
            mys.log("Environmental compatability is invalid.", withError = True)
            return


        for app in self._must_creat_apps:
            mys.log("Creating a app " + app + ".")
            self._create_app(app)
            self._create_url(app)
            self._install_app(app)

        return True


    def _create_app(self, name):
        with proj.MirageEnvironment(proj.MirageEnvironmentLevel.indjango):
            mys.command("python manage.py startapp " + name)


    def _create_url(self, name):
        with proj.InDir("./" + name):
            with open("urls.py", "a") as newscript:
                newscript.write(url_script(name))


    """
    Install created app to Django project
    """
    def _install_app(self, name):

        try:
            master_app = self.__detect_master_app()
        except:
            mys.log("Failed to detect master app.", withError = True)


        mys.log("Installing app...")

        with proj.InDir(master_app):
            if os.path.isdir("environment"):
                with proj.InDir("./environment"):
                    self.__insert_app_path(name, "common.py")

            elif os.path.isdir("settings"):
                with proj.InDir("./settings"):
                    self.__insert_app_path(name, "common.py")

            else:
                if os.path.isfile("settings.py"):
                    self.__insert_app_path(name, "settings.py")
                else:
                    mys.log("Failed to install Django app due to missing configuration file.", withError = True)


    """
    Check compatibility of Django.
    """
    def _check_all(self):

        reserved_names = (
            "test",
            "os"
        )

        for app in self._must_creat_apps:
            for name in reserved_names:
                if app == name:
                    mys.log("The app named " + app + " is reserved by Django!", withError = True)
                    raise ValueError

        for app in self._must_creat_apps:
            if os.path.isdir(app):
                mys.log("The app named " + app + " is already exists.", withError = True)
                raise FileExistsError


    def __detect_master_app(self):
        
        dirs = os.listdir(os.getcwd())

        current = os.getcwd()

        for app in dirs:

            try:
                os.chdir("./" + app)
                if os.path.isfile("settings.py"):
                    os.chdir(current)
                    return app
                else:
                    os.chdir(current)
            except: 
                pass
       
        return None


    def __insert_app_path(self, app_name, setting_file):
        lines = []
        insert_line = 0

        try:
            with open(setting_file, "r") as setting:
                try:
                    lines = setting.readlines()
                except:
                    mys.log("Failed to load configuration file lines.", withError = True)
        except:
            pass

    
        for i in range(len(lines)):
            if "INSTALLED_APPS = [" in lines[i]:
                insert_line = i
            elif "INSTALLED_APPS = (" in lines[i]:
                insert_line = i
    
        with open(setting_file, "w") as setting:
            app_config = app_name[0].upper() + app_name[1:] + "Config"
            lines.insert(insert_line + 1, "    \'" + app_name + ".apps." + app_config + "\',\n")
            setting.writelines(lines)
