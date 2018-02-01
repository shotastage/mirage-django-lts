from djconsole.flow import Workflow
from djconsole.command import log, raise_error_message
from djconsole.scaffold import server
import subprocess
import multiprocessing


class ScaffoldWorkflow(Workflow):
    
    def main(self):
        log("Launching server...")
        try:
            subprocess.Popen("djc internal_server_launch", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except:
            log("Failed to launch server!", withError = True)

        log("Launching shell...")
        try:
            subprocess.call("./shell/node_modules/.bin/electron ./shell/", shell = True)
        except:
            log("Failed to launch Electron shell!", withError = True)
