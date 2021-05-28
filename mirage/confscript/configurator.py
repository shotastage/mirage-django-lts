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

from mirage.core import Void
from mirage import system as mys

class ConfigScript():

    def __init__(self):

        # Configs
        self._enable_log: bool
        self._allow_interactive: bool

        # Setting values
        self._custom_clis = []
        self._custom_scripts = []

        # Auto exe funcs
        self.initialize()
        self.main()

    def __del__(self):
        self.deinitialize()


    def initialize(self) -> Void:
        ...


    def deinitialize(self) -> Void:
        ...

    def main(self) -> int:
        return 0


    @classmethod
    def register_prescript(self, script_path: str, target_func: str, runtime = "python") -> int:
        mys.log("Sorry, Mirage Prescript is now under construction. ; (", withError = True)
        return 0


    @classmethod
    def register_postscript(self, script_path: str, target_func: str, runtime = "python") -> int:
        mys.log("Sorry, Mirage Prescript is now under construction. ; (", withError = True)
        return 0


    def register_custom_command(self, cli: str, option: str, script_path: str) -> int:
        self._custom_clis.append((cli, option, script_path))

    def register_custom_command_with_runtime(self, cli: str, script_path: str, runtime: str) -> int:
        self._custom_scripts.append((cli, script_path, runtime))


    def execute(self, cli: str, option: str) -> int:

        for normal_cli in self._custom_clis:
            pass

        for runtime_cli in self._custom_scripts:
            pass


    @staticmethod
    def assertBool() -> bool:
        return True
