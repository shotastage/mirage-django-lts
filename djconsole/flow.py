from djconsole import console

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


class ExcuteFlow():

    def __init__(self):
        pass

    dict = {
        
    }
