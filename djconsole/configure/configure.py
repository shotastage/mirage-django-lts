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

from djconsole          import fileable
from djconsole.flow     import Workflow
from djconsole.command  import log, raise_error_message
from djconsole.command  import command

from djconsole.projectstartup.djfile import create_djfile


class ConfigureWorkFlow(Workflow):

    def main(self):
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
