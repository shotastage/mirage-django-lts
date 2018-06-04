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

import platform
import sys
import textwrap


def src(proj_name, proj_ver, proj_author, author_email,
            git_url, proj_license, proj_desc, copyrightors):

    return textwrap.dedent(
'''
from mirage import system as mys
from mirage.core import Void
from mirage.confscript import ConfigScript
from mirage.confscript.settings import Settings


MIRAGE_CONFIG_SCRIPT_VERSION = "0.0.1"
MIRAGE_CONFIG_DEFAULT_CLASS = "MirageConfig"


class MirageConfig(ConfigScript):

    BASIC_PROJECT = {
        "NAME": "{{PROJECT_NAME}}",
        "VERSION": "{{PROJECT_VERSION}}",
        "AUTHOR": "{{AUTHOR_NAME}} <{{AUTHOR_EMAIL}}>",
        "GIT_URL": "{{GIT_REPO_URL}}",
        "LICENSE": {{LICENSE_NAME}},
        "DESCRIPTION": "{{DESCRIPTION}}",
    }

    DJANGO_PROJECT = {
        "path": "{{PROJECT_NAME}}",
        "module": "{{PROJECT_NAME}}",
        "package": Settings.PackageManager.pipenv,
        "database": Settings.Database.PostgreSQL,
    }

    FRONT_END_PROJECT = {
        "path": Settings.Path.default,
        "package": Settings.PackageManager.yarn,
        "builder": Settings.Builder.Webpack,
    }

    COPYRIGHT = {
        "start_year": {{YEAR_NOW}},
        "license_doc": "{{LICENSE_URL}}",
        "copyrightors": [
            {{COPYRIGHTORS}}
        ]
    }


    def initialize(self) -> Void:
        mys.log("PINNA Setting Script V0.0.1")


    def main(self) -> int:
        self.register_custom_command("custom_cli", None, "tools/scripts/cli.py")
        self.register_custom_command_with_runtime("custom_cli_rb", "tools/scripts/ruby.rb", "ruby")

        return 0


    def deinitialize(self) -> Void:
        mys.log("Bye : )")

''').format(
    PROJECT_NAME        = proj_name,
    PROJECT_VERSION     = proj_ver,
    AUTHOR_NAME         = proj_author,
    AUTHOR_EMAIL        = author_email,
    GIT_REPO_URL        = git_url,
    PROJECT_LICENSE     = proj_license,
    PROJECT_DESC        = proj_desc,
    MODULE_NAME         = proj_name,
    COPYRIGHT_START     = get_start_year(),
    COPYRIGHTOR         = copyrightors
).strip()


def get_start_year():
    pass
