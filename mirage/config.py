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
import json
from mirage import system as sys

def get_all_config():
    sys.warn("mirage.config.get_all_config will be deprecated on next version.", PendingDeprecationWarning)
    return load_miragefile()


def get_proj_config(conf_name):
    sys.warn("mirage.config.get_proj_config will be deprecated on next version.", PendingDeprecationWarning)
    try:
        data = load_miragefile()

        if os.path.exists("Miragefile.addon"): additional = load_additional_conf()
        elif os.path.exists("Miragefile.secret"):   secret = load_secret_conf()
    except:
        return "Invalid Miragefile"

    if conf_name == "all":
        return data

    elif conf_name == "name":
        return data["project"]["name"]

    elif conf_name == "version":
        return data["project"]["version"]

    elif conf_name == "author":
        return data["project"]["author"]

    elif conf_name == "git":
        return data["project"]["git"]

    elif conf_name == "license":
        return data["project"]["license"]

    elif conf_name == "description":
        return data["project"]["description"]
        
    elif conf_name == "iyashi":
        try:
            return additional["additional_options"]["iyashi"]
        except:
            return False



def get_django_config(conf_name):
    sys.warn("mirage.config.get_django_config will be deprecated on next version.", PendingDeprecationWarning)
    try:
        data = load_miragefile()
    except:
        return "Invalid Miragefile"

    if conf_name == "path":
        if data["django"]["path"] == ".": return os.getcwd()
        else: return data["django"]["path"]

    elif conf_name == "package":
        return data["django"]["package"]

    elif conf_name == "database":
        return data["django"]["database"]




def get_node_config(conf_name):
    sys.warn("mirage.config.get_node_config will be deprecated on next version.", PendingDeprecationWarning)
    try:
        data = load_miragefile()
    except:
        return "Invalid Miragefile"

    if conf_name == "path":
        if data["frontend"]["path"] == ".": return os.getcwd()
        else: return data["frontend"]["path"]

    elif conf_name == "package":
        return data["frontend"]["package"]

    elif conf_name == "builder":
        return data["frontend"]["builder"]



def load_miragefile():
    sys.warn("mirage.config.load_miragefile will be deprecated on next version.", PendingDeprecationWarning)
    with open("Miragefile", "r") as djfile:
        try:
            return json.load(djfile)
        except:
            raise Exception


def load_additional_conf():
    sys.warn("mirage.config.load_additional_conf will be deprecated on next version.", PendingDeprecationWarning)
    with open("Miragefile.addon", "r") as djfile:
        try:
            return json.load(djfile)
        except:
            raise Exception


def load_secret_conf():
    sys.warn("mirage.config.load_secret_conf will be deprecated on next version.", PendingDeprecationWarning)
    with open("Miragefile.secret", "r") as djfile:
        try:
            return json.load(djfile)
        except:
            raise Exception
