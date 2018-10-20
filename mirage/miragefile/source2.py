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

import textwrap
import datetime


def create(proj_name, proj_ver, proj_author, author_email, git_url,
                                        proj_license, proj_desc, copyrightor):

    return textwrap.dedent('''
#
# Mirage Configuration Scripts Version 2018/03/23
# Copyright (c) 2017-2018 Shota Shimazu
# This software is licensed under the Apache v2, see LICENSE for detail.
#

from mirage import system as mys
from mirage.core import Void
from mirage.miragefile.conf import Category, Detail, Config
from mirage.confscript import ConfigScript
from mirage.confscript.settings import Settings


MIRAGE_CONFIG_SCRIPT_VERSION = "0.0.1"
MIRAGE_CONFIG_DEFAULT_CLASS = "MirageConfig"


class MirageConfig(ConfigScript):

    BASIC_PROJECT = {{
        "NAME": "{PROJECT_NAME}",
        "VERSION": "{PROJECT_VERSION}",
        "AUTHOR": "{PROJECT_AUTHOR} <{PROJECT_AUHOR_EMAIL}>",
        "GIT_URL": "{GIT_URL}",
        "LICENSE": "{PROJECT_LICENSE}",
        "DESCRIPTION": "{PROJECT_DESC}",
    }}

    DJANGO_PROJECT = {{
        "path": ".",
        "module": "{PROJECT_NAME}",
        "package": "pipenv",
        "database": "PostgreSQL",
    }}

    FRONT_END_PROJECT = {{
        "path": "shell",
        "package": "yarn",
        "builder": "webpack",
    }}

    COPYRIGHT = {{
        "start_year": {COPYRIGHT_START},
        "copyrightors": [
            "{COPYRIGHTOR}",
        ]
    }}



    def initialize(self) -> Void:
        mys.log("Mirage Setting Script v0.0.1")


    def main(self) -> int:
        # Add custom CLI script written in Python3
        # self.register_custom_command("custom-command", "<option>", "tools/scripts/custom_script.py")

        # Add custom CLI script written in other programming language.
        # self.register_custom_command_with_runtime("custom-command", "tools/scripts/custom_script.rb", "ruby")

        return 0


    def deinitialize(self) -> Void:
        mys.log("Bye : )")

''').format(
    PROJECT_NAME        = proj_name,
    PROJECT_VERSION     = proj_ver,
    PROJECT_AUTHOR      = proj_author,
    PROJECT_AUHOR_EMAIL = author_email,
    GIT_URL             = git_url,
    PROJECT_LICENSE     = proj_license,
    PROJECT_DESC        = proj_desc,
    MODULE_NAME         = proj_name,
    COPYRIGHT_START     = get_start_year(),
    COPYRIGHTOR         = copyrightor,
).strip()


def get_start_year():
    return datetime.datetime.now().strftime("%Y")
