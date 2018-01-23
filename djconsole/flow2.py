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

from djconsole.command import log

class AbstractFlow():
    def __init__(self):
        self._flows = []

    def excute(self):
        pass

    def add_flow(self, flow_instance, cmd_arg):
        pass


class Flow():

    def __init__(self):
        self._flows = []

    def flow(self):

        for flow in self._flows:
            if "function" in str(type(flow)):
                try:
                    flow()
                except:
                    raise Exception
            else:
                log(str(flow) + " is not function!", withError = True)


    def execute(self):
        self.flow()

    def register(self, *funcs):
        for func in funcs:
            self._flows.append(func)
