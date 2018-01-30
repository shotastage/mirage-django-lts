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
import shutil
import sys
import distutils

from djconsole.command      import log, raise_error_message
from djconsole              import project
from djconsole.flow         import Workflow
from djconsole.database     import DBConnection



class DjangoBackupAppWorkFlow(Workflow):
    def additional_init_(self):
        self._app_name = self._values[0]
        log(self._app_name)

    def main(self):
        self._create_buckup_dir()
        self._create_working_dir()
        self._copy_app(self._app_name)
        self._archive_dir(self._app_name)

    def _create_buckup_dir(self):
        log("Preparing backup directory...")
        if project.isproject():
            if not os.path.isdir(".djc/backup/"):
                try:
                    os.makedirs(".djc/backup/")
                except:
                    log("Failed to prepare .djc/backup with unknown error.", withError = True, errorDetail = str(os.listdir()))
            else:
                log("OK")
    

    def _create_working_dir(self):
        log("Preparing working directory...")
        if project.in_project():
            if not os.path.isdir(".djc/cache/"):
                try:
                    os.makedirs(".djc/cache/")
                except:
                    log("Failed to prepare .djc/cache with unknown error.", withError = True)
            else:
                log("OK")


    def _copy_app(self, app_name):
        log("Copying app...")
        try:
            distutils.dir_util.copy_tree(app_name, ".djc/cache/" + app_name)
        except:
            log("Failed to copy app!", withError = True, errorDetail = raise_error_message(self._copy_app))


    def _archive_dir(self, app_name):
        log("Archiving app...")
        shutil.make_archive(".djc/cache/" + app_name, "zip")

    def _prepare_db(self):
        pass
