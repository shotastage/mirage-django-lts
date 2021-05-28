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

from mirage          import fileable
from mirage.flow     import Workflow
from mirage.command  import log
from mirage.miragefile import source
from mirage.configure.miragefile import create_additional


class ConfigureWorkFlow(Workflow):

    def constructor(self):
        self._configure_target = self._option

    def main(self):
        if self._configure_target == "addon":
            self._configure_addition()
        elif self._configure_target == "secret":
            self._configure_secret()
        else:
            self._configure()

    def _configure(self):

        if fileable.exists("Miragefile"):
            if log("Miragefile is exists. Are you sure to overwrite Miragefile?", withConfirm = True):
                os.remove("Miragefile")
            else:
                log("Miragefile is already exists!", withError = True)
                raise FileExistsError
                return


        app_name     = log("App name", withInput = True)
        version      = log("App version", withInput = True)
        author       = log("Author name", withInput = True)
        email        = log("Email", withInput = True)
        git_url      = log("Git URL", withInput = True)
        license_name = log("License", withInput = True)
        description  = log("Description", withInput = True)
        copyrightor  = log("Copyrightor", withInput = True, default = author)


        with open("Miragefile", "w") as f:
            f.write(source.create(app_name, version, author, email, git_url, license_name, description, copyrightor))

    def _configure_addition(self):
        if fileable.exists("Miragefile.addon"):
            if log("Miragefile (Additional) is exists. Are you sure to overwrite?", withConfirm = True):
                os.remove("Miragefile.addon")
            else:
                log("Miragefile is already exists!", withError = True)
                raise FileExistsError
                return

        option_string = log("Additional option string", withInput = True)

        with open("Miragefile.addon", "w") as f:
            f.write(create_additional(option_string))


    def _configure_secret(self):
        with open("Miragefile.secret", "w") as f:
            f.write("")
