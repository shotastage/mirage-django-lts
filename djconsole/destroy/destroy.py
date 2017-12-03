from djconsole.command import log
from djconsole.flow import Flow
from djconsole.destroy import app
from djconsole.project import isproject

class DjangoDestroyFlow(Flow):    
    
    def __init__(self, target, args):
        self._must_target = target
        self._must_destroy = args[0]

    def flow(self):
        if str(self._must_target) == "app":
            if isproject: self._destroy_app()
        else:
            log("No destroy strategy for " + str(self._must_target) + ".", withError = True)

    def _destroy_app(self):
        log("Destroying app...")
        app._backup(self._must_destroy)
        app._destroy(self._must_destroy)
