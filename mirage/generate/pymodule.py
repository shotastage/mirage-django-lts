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

from pathlib import Path
from mirage.core import Void
from mirage import system as mys
from mirage.proj import InDir
from mirage.flow import Workflow


class ModuleCreateFlow(Workflow):

    def constructor(self) -> Void:
        self._module_name: str = self._values[0]


    def main(self) -> bool:

        if Path("self._module_name").is_dir():
            mys.log("Module {0} is already exists!".format(self._module_name), withError = True)

        else:

            mys.log("Generating \"{0}\" module...".format(self._module_name))
            Path(self._module_name).mkdir()

            with InDir(self._module_name):
                open("__init__.py", "a")

        return True
