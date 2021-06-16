# -*- coding: utf-8 -*-
"""
Copyright 2017-2020 Shota Shimazu.

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

from mirage.djargparse import ArgumentsParser


def main():

    parser = ArgumentsParser()

    # Usage & Version
    parser.add_argument("h", "help", None, "UsageShow")
    parser.add_argument("v", "version", None, "VersionShow")

    # Commands
    parser.add_argument("new", "newproject", None, "Startup")
    parser.add_argument_with_subaction("new", "newproject", "react", None, "ReactStartup")
    parser.add_argument_with_subaction("new", "newproject", "ng", None, "NgStartupWorkFlow")
    parser.add_argument_with_subaction("new", "newproject", "mini", None, "MirageMinimumStartupWorkFlow")

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

    parser.add_argument("g", "generate", "module", "ModuleCreateFlow")

    parser.add_argument("heroku", "heroku", "configure", "DjangoHerokuConfigure")

    parser.add_argument("m", "manage", None, "DjangoManagePy")

    parser.add_argument("s", "server", None, "DjangoDebugServer")
    parser.add_argument("browser", "internal-browser", None, "DjangoLaunchBrowser")

    parser.add_argument("t", "transfer", None, "MirageTransfer")

    parser.add_argument("+", "confscript", None, "MirageConfigScriptFlow")

    parser.add_argument("?", "inquiry", "update", "UpdateCheckFlow")
    parser.add_argument("?", "inquiry", "system", "SystemCheckFlow")

    # Excute
    parser.parse()
