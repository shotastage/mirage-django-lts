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
import time
import distutils

from mirage import system as mys
from mirage import proj

from mirage              import project
from mirage              import fileable
from mirage.flow         import Workflow
from mirage.database     import DBConnection

from mirage.workspace import storage

class DjangoBackupAppWorkFlow(Workflow):

    def additional_init_(self):
        self._app_name = self._values[0]


    def main(self):

        storage.MirageWorkspace.initialize()
        storage.MirageWorkspace.persist(self._app_name, "mi_backup")
        
        """
        try:
            self._check_mirage_workspace()
            self._create_buckup_dir()
            self._create_working_dir()
            self._copy_app()
            self._save_backup(self._archive_dir())
            self._clean_cache()

            mys.log("Backup completed.")

        except:
            mys.log("Failed to backup " + self._app_name + ".", withError = True)
        """


    def _check_mirage_workspace(self):

        if not fileable.exists(self._app_name):
            mys.log("The app name " + self._app_name + " is not exists!", withError = True)
            raise Exception
    

    def _create_buckup_dir(self):

        with proj.MirageEvironmet(proj.MirageEvironmetLevel.inproject):
            mys.log("Preparing backup directory...")
        
            if not fileable.exists(".mirage/persistences/backup/"):
                try:
                    fileable.mkdir(".mirage/persistences/backup/")
                except:
                    mys.log("Failed to prepare .mirage/persistences/backup with unknown error.", withError = True, errorDetail = str(os.listdir()))
            else:
                mys.log("OK")
    

    def _create_working_dir(self):
        with proj.MirageEvironmet(proj.MirageEvironmetLevel.inproject):
            mys.log("Preparing working directory...")

            if not fileable.exists(".mirage/cache/"):
                try:
                    os.makedirs(".mirage/cache/")
                except:
                    mys.log("Failed to prepare .mirage/cache with unknown error.", withError = True)
            else:
                mys.log("OK")


    def _copy_app(self):

        app_path = os.getcwd() + self._app_name
        
        mys.log("Copying app...")

        with proj.MirageEvironmet(proj.MirageEvironmetLevel.inproject):
            try:
                fileable.copy(app_path, ".mirage/cache/" + self._app_name)
            except:
                if mys.log("Old cache is exists! Are you sure to continue overwritting?", withConfirm = True):
                    fileable.copy(self._app_name, ".mirage/cache/" + self._app_name, force = True)
            else:
                mys.log("Failed to backup!", withError = True)


    def _archive_dir(self):
        with proj.MirageEvironmet(proj.MirageEvironmetLevel.inproject):
            
            mys.log("Archiving app...")
            filename = self._app_name + str(time.time())
            shutil.make_archive(".mirage/cache/" + filename, "zip")
            
            return filename


    def _save_backup(self, filename):
        
        with proj.MirageEvironmet(proj.MirageEvironmetLevel.inproject):
            fileable.move(".mirage/cache/" + filename + ".zip", ".mirage/backup/")


    def _clean_cache(self):

        with proj.MirageEvironmet(proj.MirageEvironmetLevel.inproject):
            mys.log("Cleaning...")
            fileable.rm(".mirage/cache/" + self._app_name)


    def _prepare_db(self):
        mys.log("This is not implemented!")
