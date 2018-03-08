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
from pathlib import Path
from mirage.flow import Workflow
from mirage import proj
from mirage import system as mys


class DjangoMergeMigrationWorkFlow(Workflow):

    def main(self):
        mys.log("Merging all migrations...")

        if mys.log(
            "Are you sure to merge all migrations? This operation will delete all migration files!"
            ,withConfirm = True):
            self._merge()
        else:
            mys.log("Canceled")


    def _merge(self):
        with proj.MirageEnvironment(proj.MirageEnvironmentLevel.inapp):
            mys.log("Integrate migrations...")

            with proj.InDir("migrations"):
                path_obj = Path(os.getcwd())
                migration_script_path = path_obj.glob("*.py")

                for path in migration_script_path:
                    if not "__init__.py" in str(path):
                        mys.log("Removing " + str(path) + "!")
                        os.remove(path)
                
            with proj.MirageEnvironment(proj.MirageEnvironmentLevel.indjango):
                os.system("python manage.py makemigrations")
