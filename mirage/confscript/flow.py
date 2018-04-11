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

import sys, os, imp
from mirage.flow import Workflow
from mirage import system as mys
from mirage.proj import MirageEnvironment, MirageEnvironmentLevel



class MirageConfigScriptFlow(Workflow):

    global config_script

    def constructor(self):
        self._cli = ""
        self._option = ""


    def main(self) -> bool:
        mys.log("Now under construction.")
        return

        with MirageEnvironment(MirageEnvironmentLevel.inproject):

            try:
                instance = self.load_script()
            except:
                return False

            instance.execute(self._cli, self._option)

        return True


    def load_script(self) -> object:

        sys.path.append(os.getcwd())

        try:
            fp, name, desc = imp.find_module("mirage.config")
            config_script = imp.load_module("config_script", fp, name, desc)

            if config_script.MirageConfig.assertBool():
                mys.log("Config script loaded!")
            else:
                mys.log("Failed to import mirage.config.py !", withError = True)
                raise ImportError

        except ImportError:
            mys.log("Failed to import mirage.config.py !", withError = True)


    def check_conf_script_version(self) -> bool:
        pass
