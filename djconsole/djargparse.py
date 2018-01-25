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

class ArgumentsParser():

    def __init__(self, usage, version):

        # Doc strings
        self._usage = None
        self._version = None
        self._add_doc_string()

        # Command
        self._command_list = []
        
        # Arguments
        self._sub_action = None
        self._option = None
        self._values = None
        self._set_arguments_from_cli()

        # Function
        self._excute = self.dammy_colon_action(self._sub_action, self._values)



    def add_argument(self, shorten_cmd, long_cmd, option = None, execute = None, strategy = ParsingStrategies.default):
        self._command_list.append((shorten_cmd, long_cmd, execute))

    def add_cmd_with_action(self, shorten_cmd, long_cmd, subaction):
        pass


    def parse(self):
        self._excute(self._sub_action, self._values)

    def dammy(self, option, values):
        print("This is dammy function.")

    def dammy_colon_action(self, option, values):
        print("This is dammy function.")

    def _colon_separate(self, cmd_colon_value):
        pass
    
    def _set_arguments_from_cli(self):
        args = sys.argv.pop(0)
        self._option = args[0]
        self._values = args[1:-1]


    def _add_doc_string(self):
        self._usage = """
Django Console Arguments Parser
Copyright 2017-2018 Shota Shimazu.

This command line tools does not define usage or help!
                      """

        self._version = """
Django Console Arguments Parser
Version 0.0.1

Copyright 2017-2018 Shota Shimazu.
This software is licensed under the Apache v2, see LICENSE for detail.
                        """



class ParsingStrategies(enum.Enum):
    default = 0
    colon   = 1



def compatible_with_argparse(*reserved_args):

    def _decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for reserve in reserved_args:
                if args[1] == reserve:
                    re = func(*args, **kwargs)
                    return re
        return wrapper
    return _decorator
