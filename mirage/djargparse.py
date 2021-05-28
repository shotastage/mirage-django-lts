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

import sys
import functools
from mirage.core import Void
from mirage import system

# Flow Classies
from mirage import workflows


class ArgumentsParser(object):

    def __init__(self):

        # Arguments
        self._cmd = None            # ex. **new**
        self._sub_action = None     # ex. new:**cms**
        self._option = None         # ex. g **app**
        self._option_detail = None  # ex. g app **--basic**
        self._values = None         # ex. g **app api mail user**
        self.__insert_arguments()   # <== Insert real value

        # Exec flow
        self._exec_flow = None

        # Arguments Array
        self._arguments = (
            self._cmd,
            self._sub_action,
            self._option,
            self._option_detail,
            self._values
        )

        # Is Assessmented
        self._assessmented = False



    def add_argument(self, shorten_cmd: str, long_cmd: str, option: str, execute: str) -> Void:

        if self._assessmented: return

        # Check command

        if not self._cmd == shorten_cmd and not self._cmd == long_cmd:
            return

        if not self._sub_action is None:
            return

        if not option is None:
            if self._option == option:
                self._exec_flow = execute
                self._assessmented = True
        else:
            self._exec_flow = execute
            self._assessmented = True

        return


    def add_argument_with_subaction(self, base_shorten_cmd: str,
                                    base_long_cmd: str, action: str, option: str, execute: str) -> Void:

        if self._assessmented: return

        if not self._cmd == base_shorten_cmd and not self._cmd == base_long_cmd:
            return

        if not self._sub_action == action:
            return

        if not option is None:
            if self._option == option:
                self._exec_flow = execute
                self._assessmented = True
        else:
            self._exec_flow = execute
            self._assessmented = True


        return


    def parse(self) -> Void:
        # If there are no command, show usage.
        if len(sys.argv) == 1:
            instance = getattr(workflows, "UsageShow")(self._arguments)
            instance.run()
            return

        # Check excute function is not empty.
        if not self._exec_flow == None:
            instance = getattr(workflows, self._exec_flow)(self._arguments)
            instance.run()
            return

        else:
            system.log("Unable to invoke action \"{0}\"!".format(sys.argv[1]), withError = True)
            instance = getattr(workflows, "UsageShow")(self._arguments)
            instance.run()


    def __insert_arguments(self):
        # Get main command **new**:cms
        try: self._cmd = self.__colon_separate_cmd(sys.argv[1])
        except: pass

        # Get subaction new:**cms**
        try: self._sub_action = self.__colon_separate_action(sys.argv[1])
        except: pass

        # Get option and detail option
        # optin =           mi g **app**
        # detail option =   mi g app **--basic**
        try:
            self._option = sys.argv[2]

            if "--" in sys.argv[3]:
                self._option_detail = sys.argv[3]
        except: pass

        # Get values
        try:
            if "--" in sys.argv[3]:
                self._values = sys.argv[4:]
            else:
                self._values = sys.argv[3:]
        except: pass


    def __colon_separate_cmd(self, cmd_colon_value: str) -> str:
        if ":" in cmd_colon_value:
            return cmd_colon_value.split(":")[0]
        else:
            return cmd_colon_value


    def __colon_separate_action(self, cmd_colon_value: str) -> str:
        if ":" in cmd_colon_value:
            return cmd_colon_value.split(":")[1]
        else:
            raise ValueError



class DetailOptionParser():

    def __init__(self, detail_option):
        self._option_detail = detail_option
        self._excute = None

    def add_argument(self, option, excute):
        if self._option_detail == option:
            self._excute = excute

    def parse(self):
        self._excute.excute()



def reserve_as_command(*reserved_args):

    def _decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for reserve in reserved_args:
                if args[1] == reserve:
                    re = func(*args, **kwargs)
                    return re
        return wrapper
    return _decorator
