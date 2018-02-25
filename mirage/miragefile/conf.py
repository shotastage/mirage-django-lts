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
import enum
import yaml
from mirage import proj
from mirage import system as sys


class Category(enum.Enum):
    project_basic   = 0
    django          = 1
    frontend        = 2
    workspace       = 3
    copyright       = 4


class Detail(enum.Enum):
    project_name    = 0
    project_version = 1
    project_author  = 2
    project_git     = 3
    project_license = 4
    project_description = 5
    django_path     = 6
    django_module   = 7
    django_package_manager = 8
    django_db_backend = 9


class Config():

    def __init__(self, file_type = None):

        with proj.MirageEvironmet(proj.MirageEvironmetLevel.inproject):
            if file_type == "secret":
                self._data = self._load_yaml("Miragefile.secret")
            elif file_type == "addon":
                self._data = self._load_yaml("Miragefile.addon")
            elif file_type == None:
                self._data = self._load_yaml("Miragefile")
            else:
                sys.log("Wrong configuration type {0}.".format(file_type), withError = True)


    def get(self, category, detail):
        
        if category == Category.project_basic:
            return self._get_project(detail)
        if category == Category.django:
            return self._get_django(detail)



    def _get_project(self, detail):
       
        if detail == Detail.project_name:
            return self._data["project"]["name"]
        elif detail == Detail.project_version:
            return self._data["project"]["version"]
        elif detail == Detail.project_author:
            return self._data["project"]["author"]
        elif detail == Detail.project_git:
            return self._data["project"]["git"]
        elif detail == Detail.project_license:
            return self._data["project"]["license"]
        elif detail == Detail.project_description:
            return self._data["project"]["description"]
        else:
            sys.log("The config information named " + str(detail) + " does not exist!", withError = True) 
            return self._load_failed()


    def _get_django(self, detail):

        if detail == Detail.django_path:
            return self._data["project"]["django"]["path"]
        elif detail == Detail.django_module:
            return self._data["project"]["django"]["module"]
        elif detail == Detail.django_package_manager:
            return self._data["project"]["django"]["package"]
        elif detail == Detail.django_db_backend:
            return self._data["project"]["django"]["database"]
        else:
            sys.log("The config information named " + str(detail) + " does not exist!", withError = True) 
            return self._load_failed()


    def _load_yaml(self, filename):

        if not os.path.exists(filename):
            sys.log("Failed to find Miragefile!", withError = True)
            raise FileNotFoundError

        with open(filename, "r") as yamlfile:
            try: 
                return yaml.load(yamlfile)
            except:
                sys.log("Failed to load Miragefile!", withError = True, errorDetail = sys.raise_error_message(self._load_yaml))
                return self._load_failed()
    

    def _load_failed(self):
        return "Invalid Miragefile"


"""
#
# BACKUP
#
#


def get_copyright(item):

    data = load_miragefile()

    if item == MiragefileDataCategory.copyright_start_year:
        return data["project"]["copyright"]["start_year"]
    elif item == MiragefileDataCategory.copyright_copyrigtors:
        return data["project"]["copyright"]["copyrightors"]
    else:
        log("The config information named " + item + " does not exist!", withError = True) 
        return load_failed()


def get_private_profile(item):

    data = load_miragefile_secret()

    if item == "name":
        return data["private_profile"]["name"]
    elif item == "license":
        return data["private_license"]["url"]
    else:
        log("The config information named " + item + " does not exist!", withError = True) 
        return load_failed()



def get_reserved_addon_config(item):

    data = load_miragefile_addon()

    if item == "iyashi":
        try:
            return data["additional_options"]["iyashi"]
        except:
            return False
    else:
        log("The config information named " + item + " does not exist!", withError = True) 
        return load_failed()
"""
