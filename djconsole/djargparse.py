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
import enum
import functools
from djconsole.command import log

# Flow Classies
from djconsole import workflows


class ArgumentsParser(object):

    def __init__(self):
        
        # Arguments
        self._cmd = None            # ex. **new**
        self._sub_action = None     # ex. new:**cms**
        self._option = None         # ex. g **app**
        self._option_detail = None  # ex. g app **--basic**
        self._values = None         # ex. g **app api mail user**
        self.__insert_arguments()   # <== Insert real value 

        # Arguments Array 
        self._arguments = [
            self._cmd,
            self._sub_action,
            self._option,
            self._option_detail,
            self._values,
        ]

        # Exec flow
        self._exec_flow = None



    def add_argument(self, shorten_cmd, long_cmd, option, execute):
        if self._cmd == shorten_cmd or self._cmd == long_cmd:
            if self._sub_action == None:
                self._exec_flow = execute

        return
    

    def add_argument_with_subaction(self, base_shorten_cmd, base_long_cmd, action, option, execute):
        if self._cmd == base_shorten_cmd or self._cmd == base_long_cmd:
            if self._sub_action == action:
                self._exec_flow = execute

        return


    def parse(self):
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
            log("CLI action is not appended!", withError = True)


    def __insert_arguments(self):
        # Get main command **new**:cms
        try: self._cmd = self.__colon_separate_cmd(sys.argv[1])
        except: pass

        # Get subaction new:**cms**
        try: self._sub_action = self.__colon_separate_action(sys.argv[1])
        except: pass
        
        # Get option and detail option
        # optin =           djc g **app**
        # detail option =   djc g app **--basic**
        try:
            if "--" in sys.argv[2]:
                self._option_detail = sys.argv[2]
                self._option = sys.argv[3]
            else:
                self._option = sys.argv[2]
        except: pass

        # Get values
        try:
            if "--" in sys.argv[2]:
                self._values = sys.argv[3: -1]
            else:
                self._values = sys.argv[2: -1]
        except: pass


    def __colon_separate_cmd(self, cmd_colon_value):
        if ":" in cmd_colon_value:
            return cmd_colon_value.split(":")[0]
        else:
            return cmd_colon_value


    def __colon_separate_action(self, cmd_colon_value):
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
