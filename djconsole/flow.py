from djconsole.command import log



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

    def register(*funcs):
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
            log("これファよな", withError = True)
            func()
            return
    

        if self._action_target == None:
            if not self.args == []:
                try:
                    func(self.args)
                except:
                    print(self.args)
                    log("Failed to excute " + str(func) + " .", withError = True)
                    log("1")
            else:
                try:
                    func()
                except:
                    log("Failed to excute " + str(func) + " .", withError = True)
                    log("2")
            return

        if self.args == None:
            if not self._action_target == None:
                try:
                    func(self._action_target)
                except:
                    log("Failed to excute " + str(func) + " .", withError = True)
                    log("3")
            else:
                try:
                    func()
                except:
                    log("Failed to excute " + str(func) + " .", withError = True)
                    log("4")
            return


class ActionLists():

    def __init__(self, action, action_target, args, switch):
        self.action = action
        self._action_target = action_target
        self.args = args
        self.switch = switch
        self.funcs = []
