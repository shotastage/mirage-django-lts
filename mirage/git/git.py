# -*- coding: utf-8 -*-
"""
Copyright 2017 Shota Shimazu.

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
from mirage.command import log
from mirage.command import command


class DjangoGitFlow(Flow):

    def __init__(self, subcommand):
        log("Django Console Git is now unser development!", withError = True)
        self._subcommand = subcommand

    def flow(self):
        os.system("git " + self._subcommand)

    def _pull(self):
        command("git pull origin master")

    def _puash(self):
        command("git push -u origin master")
