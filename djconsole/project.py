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
import warnings
from djconsole.command import log


# New
import sys

def in_project():
    try:
        set_import_root()

        import manage

        return True
    except ImportError:
        return False

def in_app():
    set_import_root()

    try:
        import apps

        return True
    except ImportError:
        return False

def set_import_root():
    sys.path.append("./")




# Old
def isproject():
    warnings.warn(
            "project.isproject will be depricated on next version!",
            PendingDeprecationWarning)
    
    if os.path.isfile("manage.py"):
        return True
    else:
        return False

def project_name():
    if isproject:

        contents = os.listdir(os.getcwd())

        for test in contents:
            if os.path.isdir(test):
                current = os.getcwd()
                os.chdir(test)
                if os.path.isfile("settings.py"):
                    return str(test)
                os.chdir(current)
