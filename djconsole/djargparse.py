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

class ArgumentsParser():

    def __init__(self, usage, version):
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
        self._excute_func = self.dammy()


    def add_argument(self, shorten_cmd, long_cmd, values, strategy = ParsingStrategies.default):
        if strategy == ParsingStrategies.default:
            pass
        elif strategy == ParsingStrategies.colon:
            pass
        elif strategy == ParsingStrategies.subcommand:
            pass


    def parse(self):
        pass


    def _colon_separate(self, cmd_colon_value):
        pass


    def dammy(self):
        print("This is dammy function.")


class ParsingStrategies(enum.Enum):
    default = 0
    colon   = 1
    subcommand = 2