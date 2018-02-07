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
from mirage.command  import log, raise_error_message
from mirage.command  import command

from mirage.projectstartup.djfile import create_djfile
from mirage.configure.djfile import create_additional


class ConfigureWorkFlow(Workflow):

    def additional_init_(self):
        self._configure_target = self._option
        log(str(self._configure_target))

    def main(self):
        if self._configure_target == "addition":
            self._configure_addition()
        elif self._configure_target == "secret":
            self._configure_secret()
        else:
            self._configure()

    def _configure(self):

        if fileable.exists("DjFile"):
            if log("DjFile is exists. Are you sure to overwrite DjFile?", withConfirm = True):
                os.remove("DjFile")
            else:
                log("DjFile is already exists!", withError = True)
                raise FileExistsError
                return
        
        app_name     = log("App name", withInput = True)
        version      = log("App version", withInput = True)
        author       = log("Author name", withInput = True)
        git_url      = log("Git URL", withInput = True)
        license_name = log("License", withInput = True)
        description  = log("Description", withInput = True)

        with open("DjFile", "w") as f:
            f.write(create_djfile(app_name, version, author, git_url, license_name, description))

    def _configure_addition(self):
        if fileable.exists("DjFile.additional"):
            if log("DjFile (Additional) is exists. Are you sure to overwrite?", withConfirm = True):
                os.remove("DjFile.additional")
            else:
                log("DjFile is already exists!", withError = True)
                raise FileExistsError
                return
        
        option_string = log("Additional option string", withInput = True)

        with open("DjFile.additional", "w") as f:
            f.write(create_additional(option_string))


    def _configure_secret(self):
        with open("DjFile.secret", "w") as f:
            f.write("")
