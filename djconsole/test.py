#!/usr/bin/env python

from enum import Enum

class ARG():

    def __init__(self, action, action_target, args):
        self._action = action
        self._action_target = action_target
        self.args = args
    
    def judge(self, action_name, func):
        if self._action == action_name:
            self._excute(func)

    def _excute(self, func):
        func(self._action_target, self.args)



class ActionLists():

    def __init__(self):
        pass

class CMDS(ActionLists):

        def new(self, second_action, args):
            if second_action == "app":
                print("CREATING APP")
                for arg in args:
                    print(arg)






if __name__ == "__main__":

    args = ARG("new", "app", [1, 2, 4, 6])
    cmds = CMDS()

    args.judge("new", cmds.new)
