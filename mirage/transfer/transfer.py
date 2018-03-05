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
import zipfile
from pathlib import Path
from mirage.flow import Workflow
from mirage import system as mys
from mirage import proj

class MirageTransferWorkflow(Workflow):
    
    def constructor(self):
        self._app = self._option
        self._to  = self._values[0]

    def main(self):
        
        # Logger instance

        logger = mys.progress.Progress()
        
        with proj.MirageEvironmet(proj.MirageEvironmetLevel.indjango):

            # In advance checking.
            try:
                self._check(logger)
            except:
                return

            logger.write("Searching application {0}...".format(self._app), withLazy = True)

            if Path(self._app).is_dir():
                self._compress(logger)
                self._move(logger)
                self._extract(logger)
                logger.update("Completed!")
            else:
                logger.update("Can not detect application {0}!".format(self._app))
                mys.log("Failed to transfer app {0}!".format(self._app), withError = True,
                errorDetail = mys.raise_error_message(
                    "The application diresctory does not exists!"
                ))
                return

    def _check(self, logger):

        with proj.InDir(self._to):

            if Path(self._app).is_dir():
                if not mys.log("{0} ia already exists.\nAre you sure to replace new one?", withConfirm = True):
                    raise FileExistsError
                else:
                    os.system("rm -rf " + self._app)


    def _compress(self, logger):
        logger.update("Compressing application...")
        shutil.make_archive(self._app, "zip", root_dir = os.getcwd())

    
    def _move(self, logger):
        logger.update("Transfering application...")
        shutil.move(self._app, self._to)

    def _extract(self, logger):

        with proj.InDir(self._to):
            logger.update("Extracting application...")
            with zipfile.ZipFile(self._app + ".zip", "r") as contents:
                contents.extractall()

            logger.update("Cleaning...")
            os.remove(self._app + ".zip")
