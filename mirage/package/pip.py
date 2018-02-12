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

from mirage.flow import Workflow
from mirage.command import log, raise_error_message
from mirage.command import command


class DjangoPackageWorkFlow(Workflow):

    def constructor(self):
        
        self._action = self._option
        self._packages = self._values

    def main(self):
        log("Mirage package manager...")

    def _init(self):
        ignore_packages = ["setuptools", "pip", "python"]
        already_pip = pip.utils.get_installed_distributions(local_only = True, skip = ignore_packages)


    def _install(self, package_name):
        log("Installing package " + package_name + " ...")

    def _uninstall(self, package_name):
        log("Uninstalling package " + package_name + " ...")
