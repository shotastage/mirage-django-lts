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

from djconsole.flow import Flow
from djconsole.command import log
from djconsole.command import command


class DjangoMigrateFlow(Flow):

    def __init__(self, subcommand):
        self._subcommand = subcommand

    def flow(self):
        log("Clearing all DB...")
        self._reset_db()

    def _reset_db(self):
        os.system("echo Now under development")

    def _remove_sqlite(self):
        log("Removing SQLite3 file...")
        if os.path.exists("db.sqlite3"):
            os.remove("db.sqlite3")
