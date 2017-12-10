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
import shutil

from djconsole.command  import log
from djconsole          import project
from djconsole.flow     import Flow
from djconsole.databse  import DBConnection


class DjangoBackupAppFlow(Flow):

    def __init__(self):
        pass

    def flow(self):
        self._create_buckup_dir()
        self._create_working_dir()
    

    def _create_buckup_dir(self):
        if project.isproject:
            if not os.path.isdir(".djc/backup/"):
                try:
                    os.makedirs(".djc/backup/")
                except:
                    log("Failed to prepare .djc/backup with unknown error.", withError = True)
    


    def _create_working_dir(self):
        if project.isproject:
            if not os.path.isdir(".djc/cache/"):
                try:
                    os.makedirs(".djc/cache/")
                except:
                    log("Failed to prepare .djc/cache with unknown error.", withError = True)



    def _copy_app(self, dir_name):
        shutil.copytree(dir_name, ".djc/cache/")

    def _archive_dir(self, dir_name):
        shutil.make_archive(dir_name, "zip")



## Backup
def create_buckup_dir():
    if project.isproject:
        if not os.path.isdir(".djc/backup/"):
            try:
                os.makedirs(".djc/backup/")
            except:
                log("Failed to prepare .djc/backup with unknown error.", withError = True)


def create_working_dir():
    if project.isproject:
        if not os.path.isdir(".djc/cache/"):
            try:
                os.makedirs(".djc/cache/")
            except:
                log("Failed to prepare .djc/cache with unknown error.", withError = True)
