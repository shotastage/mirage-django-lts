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

###########  WARNING  #####################################################
# This module will be discarded. Please replace new API mirage.miragefile #
###########################################################################

import os
import enum
import json
from mirage.command import log, raise_error_message


class MiragefileDataCategory(enum.Enum):
    project_name = 0
    project_version = 1
    project_author = 2
    project_git = 3
    project_license = 4
    project_description = 5
    django_path = 6
    django_module = 7
    django_package_manager = 8
    django_db_backend = 9
    front_path = 10
    front_package = 11
    front_builder = 12
    workspace_path = 13
    copyright_start_year = 14
    copyright_copyrigtors = 15


def get_project(item):
    
    data = load_miragefile()

    if item == MiragefileDataCategory.project_name:
        return data["project"]["name"]
    elif item == MiragefileDataCategory.project_version:
        return data["project"]["version"]
    elif item == MiragefileDataCategory.project_author:
        return data["project"]["author"]
    elif item == MiragefileDataCategory.project_git:
        return data["project"]["git"]
    elif item == MiragefileDataCategory.project_license:
        return data["project"]["license"]
    elif item == MiragefileDataCategory.project_description:
        return data["project"]["description"]
    else:
        log("The config information named " + item + " does not exist!", withError = True) 
        return load_failed()


def get_django(item):

    data = load_miragefile()

    if item == MiragefileDataCategory.django_path:
        return data["project"]["django"]["path"]
    elif item == MiragefileDataCategory.django_module:
        return data["project"]["django"]["module"]
    elif item == MiragefileDataCategory.django_package_manager:
        return data["project"]["django"]["package"]
    elif item == MiragefileDataCategory.django_db_backend:
        return data["project"]["django"]["database"]
    else:
        log("The config information named " + item + " does not exist!", withError = True) 
        return load_failed()


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


def load_miragefile():
    return _load_json("Miragefile")


def load_miragefile_addon():
    return _load_json("Miragefile.addon")


def load_miragefile_secret():
    return _load_json("Miragefile.secret")


def _load_json(filename):

    if not os.path.exists(filename):
        return filename + " does not exist!"

    with open(filename, "r") as jsonfile:
        try: 
            return json.load(jsonfile)
        except:
            log("Failed to load Miragefile!", withError = True, errorDetail = raise_error_message(_load_json))
            return load_failed()

def load_failed():
    return "Invalid Miragefile"
