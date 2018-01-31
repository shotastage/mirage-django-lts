# -*- coding: utf-8 -*-
"""
Copyright 2017-2018 Shota Shimazu.

This software is licensed under the MIT, see LICENSE for detail.
"""

import os
import shutil
import sys
import time
import distutils

from djconsole              import project
from djconsole              import fileable
from djconsole.command      import log, raise_error_message
from djconsole.flow         import Workflow
from djconsole.database     import DBConnection


class DjangoBackupAppWorkFlow(Workflow):
    def additional_init_(self):
        self._app_name = self._values[0]

    def main(self):
        try:
            self._check_djc_workspace()
            self._create_buckup_dir()
            self._create_working_dir()
            self._copy_app(self._app_name)
            save_file = self._archive_dir(self._app_name)
            self._save_backup(save_file)
            self._clean_cache()

            log("Backup completed.")

        except:
            log("Failed to backup " + self._app_name + ".", withError = True)


    def _check_djc_workspace(self):
        if not project.in_project():
            log("You are now out of Django project!", withError = True,
                                errorDetail = raise_error_message(self._check_djc_workspace))
        
            raise EnvironmentError

        if not fileable.exists(self._app_name):
            log("The app name " + self._app_name + " is not exists!", withError = True)
            raise Exception
    

    def _create_buckup_dir(self):
        log("Preparing backup directory...")
        if project.isproject():
            if not fileable.exists(".djc/backup/"):
                try:
                    fileable.mkdir(".djc/backup/")
                except:
                    log("Failed to prepare .djc/backup with unknown error.", withError = True, errorDetail = str(os.listdir()))
            else:
                log("OK")
    

    def _create_working_dir(self):
        log("Preparing working directory...")
        if project.in_project():
            if not fileable.exists(".djc/cache/"):
                try:
                    os.makedirs(".djc/cache/")
                except:
                    log("Failed to prepare .djc/cache with unknown error.", withError = True)
            else:
                log("OK")


    def _copy_app(self, app_name):
        log("Copying app...")
        try:
            fileable.copy(app_name, ".djc/cache/" + app_name)
        except:
            if log("Old cache is exists! Are you sure to continue overwritting?", withConfirm = True):
                fileable.copy(app_name, ".djc/cache/" + app_name, force = True)
            else:
                log("Failed to backup!", withError = True)


    def _archive_dir(self, app_name):
        log("Archiving app...")
        filename = app_name + str(time.time())
        shutil.make_archive(".djc/cache/" + filename, "zip")
        return filename


    def _save_backup(self, filename):
        fileable.move(".djc/cache/" + filename + ".zip", ".djc/backup/")


    def _clean_cache(self):
        log("Cleaning...")
        fileable.rm(".djc/cache/" + self._app_name)


    def _prepare_db(self):
        log("This is not implemented!")
