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
        try:
            self._to  = self._values[0]
        except:
            self._to = mys.log("Trasfer to", withInput = True)

    def main(self):
        # Beta Warning
        mys.log("This feature is now under Beta version.", withError=True)

        # Logger instance

        logger = mys.progress.Progress()
        
        with proj.MirageEnvironment(proj.MirageEnvironmentLevel.indjango):

            # In advance checking.
            try:
                self._check(logger)
            except:
                return

            logger.write("Searching application %s..." % self._app, withLazy = True)

            if Path(self._app).is_dir():
                mys.log(os.getcwd())
                shutil.copytree(self._app, os.path.join(self._to, self._app))
                logger.update("Completed!")
            else:
                logger.update("Can not detect application %s!" % self._app)
                mys.log("Failed to transfer app %s!" % self._app, withError = True,
                errorDetail = mys.raise_error_message(
                    "The application diresctory does not exists!"
                ))
                return

    def _check(self, logger):
        
        with proj.InDir(self._to):

            if Path(self._app).is_dir():
                if not mys.log("%s ia already exists.\nAre you sure to replace new one?" % self._app, withConfirm = True):
                    raise FileExistsError
                else:
                    os.system("rm -rf " + self._app)


    def _compress(self, logger):
        logger.update("Compressing application...")

        try:
            shutil.make_archive(self._app, "zip", root_dir = os.getcwd())
        except:
            pass
            # shutil.make_archive raises ZIP does not support timestamps before 1980
            #

    
    def _move(self, logger):
        logger.update("Transfering application...")
        shutil.move(self._app, self._to)

    def _extract(self, logger):

        with proj.InDir(self._to):
            logger.update("Extracting application...")

            try:
                with zipfile.ZipFile(self._app + ".zip", "r") as contents:
                    contents.extractall()
            except:
                pass
                # zipfile.ZipFile raises No such file or directory: 'hoge.zip'
                # But, zip file is extracted!

            logger.update("Cleaning...")
            #os.remove(self._app + ".zip")


    def _clean(self, logger):
        pass
        # mys.log(os.getcwd(), withError=True)
        # logger.update("Cleaning...")
        # os.remove(self._app + ".zip")
