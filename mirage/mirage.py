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

import sys

from mirage.djargparse import ArgumentsParser
from mirage.command import log, raise_error_message


def main():

    parser = ArgumentsParser()

    # Usage & Version
    parser.add_argument("h", "help", None, "UsageShow")
    parser.add_argument("v", "version", None, "VersionShow")

    # Commands
    parser.add_argument("new", "newproject", None, "DjangoStartup")
    parser.add_argument_with_subaction("new", "newproject", "react", None, "ReactStartup")
    parser.add_argument_with_subaction("new", "newproject", "cms", None, "DjangoCMSStartup")

    parser.add_argument("b", "backup", "app", "DjangoBackupApp")

    parser.add_argument("conf", "configure", None, "Configure")

    parser.add_argument("c", "console", None, "DjangoConsole")
    parser.add_argument_with_subaction("c", "console", "db", None, "DjangoDBConsole")

    parser.add_argument("d", "destroy", "app", "DjangoDestroy")

    parser.add_argument_with_subaction("db", "database", "migrate", None, "DjangoMigrate")
    parser.add_argument_with_subaction("db", "database", "reset", None, "DjangoDBReset")
    parser.add_argument_with_subaction("db", "database", "merge", None, "DjangoMergeMigration")

    # parser.add_argument("d", "destroy", None, "DjangoDestroy")

    parser.add_argument("g", "generate", "app", "DjangoAppMake")

    parser.add_argument("g", "generate", "model", "DjangoModelMake")

    parser.add_argument("heroku", "heroku_util", "configure", "DjangoHerokuConfigure")

    parser.add_argument("ide", "scaffold", None, "Scaffold")
    parser.add_argument("internal_server_launch", "internal_server_launch", None, "ScaffoldServer")
    parser.add_argument("internal_debug_server_launch", "internal_debug_server_launch", None, "ScaffoldDebugServer")

    parser.add_argument("m", "manage", None, "DjangoManagePy")
    
    parser.add_argument("s", "server", None, "DjangoDebugServer")
    parser.add_argument("browser", "internal-browser", None, "DjangoLaunchBrowser")

    parser.add_argument("t", "transfer", None, "MirageTransfer")

    parser.add_argument("f", "file", None, "Touch")

    # Excute
    parser.parse()
