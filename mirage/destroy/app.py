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

import shutil
import tarfile
import os
from djconsole.command import log, raise_error_message
from djconsole.backup import backup


def _check(name):
    if os.path.isdir(name):
        return
    else:
        raise FileNotFoundError


def _backup(name):
    try:
        _check(name)
    except:
        return


    backupper = backup.DjangoBackupAppWorkFlow([
            "b",
            None,
            "app",
            None,
            name
    ])

    backupper.main()

   
def _destroy(name):
    shutil.rmtree(name)