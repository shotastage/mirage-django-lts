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
import pip

from mirage.flow import Flow, Workflow
from mirage.command import log
from mirage.command import command



class DjangoPipPackageWorkFlow(Workflow):

    def additional_init_(self):
        try:
            self._project_name = self._option
        except:
            self._project_name = None
    
    def __init__(self, subcommand):
        self._subcommand = subcommand

    def main(self):
        if self._subcommand == "check":
            self._check()
        elif self._subcommand == "install":
            self._install()
        else:
            log("Unkown command " + self._subcommand + "!", withError = True)

    def _check(self):
        os.system("pip list -o")

    def _install(self):
        log("Install package from requirements.txt")
        os.system("pip install -r requirements.txt")

    def _show_package_list(self):
        pip.utils.get_installed_distributions(local_only = True)



class DjangoPipPackageFlow(Flow):

    def __init__(self, subcommand):
        self._subcommand = subcommand

    def flow(self):
        if self._subcommand == "check":
            self._check()
        elif self._subcommand == "install":
            self._install()
        else:
            log("Unkown command " + self._subcommand + "!", withError = True)

    def _check(self):
        os.system("pip list -o")

    def _install(self):
        log("Install package from requirements.txt")
        os.system("pip install -r requirements.txt")
