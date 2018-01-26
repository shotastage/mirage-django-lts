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


class AbstractFlow2():
    def __init__(self):
        self._flows = []

    def excute(self):
        pass

    def add_flow(self, flow_instance, cmd_arg):
        pass


class Flow2():

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




class Flow():

    def __init__(self, onInstance = False):
        self._flows = []

        if onInstance:
            self.flow()

    def flow(self):

        for flow in self._flows:
            if "function" in str(type(flow)):
                try:
                    flow()
                except:
                    raise Exception

    def execute(self):
        self.flow()

    def register(self, *funcs):
        for func in funcs:
            self._flows.append(func)



class GatheredArgs():

    def __init__(self, action, action_target, args):
        self.action = action
        self._action_target = action_target
        self.args = args



""" Backup """
class ArgumentSwitch():

    def __init__(self, action, action_target, args):
        self._action = action
        self._action_target = action_target
        self.args = args


    def judge(self, func, *action_names):
        for action_name in action_names:
            if self._action == action_name:
                self._excute(func)
                return True
        
        return False

    def _excute(self, func):

        if self._action_target == None and self.args == []:
            func()
            return
    

        if self._action_target == None:
            if not self.args == []:
                try:
                    func(self.args)
                except:
                    print(self.args)
                    log("Failed to excute " + str(func) + " .", withError = True)
            else:
                try:
                    func()
                except:
                    log("Failed to excute " + str(func) + " .", withError = True)
            return

        if self.args == None:
            if not self._action_target == None:
                try:
                    func(self._action_target)
                except:
                    log("Failed to excute " + str(func) + " .", withError = True)
            else:
                try:
                    func()
                except:
                    log("Failed to excute " + str(func) + " .", withError = True)
            return


class ActionLists():

    def __init__(self, action, action_target, args, switch):
        self.action = action
        self._action_target = action_target
        self.args = args
        self.switch = switch
        self.funcs = []
