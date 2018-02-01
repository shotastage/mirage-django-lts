from djconsole.flow import Workflow
from djconsole.command import log, raise_error_message
from djconsole.scaffold import server
import subprocess
import multiprocessing
from time import sleep


class ScaffoldWorkflow(Workflow):
    
    def main(self):

        server = None
        shell = None
        
        log("Launching server...")
        try:
            server = subprocess.Popen("djc internal_server_launch", stdout=subprocess.PIPE, shell=True)
        except:
            log("Failed to launch server!", withError = True)

        log("Launching shell...")
        try:
            sleep(3)
            shell = subprocess.Popen("./shell/node_modules/.bin/electron ./shell/", stdout=subprocess.PIPE, shell=True)

            shell.wait()

            try:
                server.terminate()
            except:
                log("Failed to terminate server!", withError = True)
            
            try:
                shell.terminate()
            except:
                log("Failed to terminate shell.", withError = True)
        except:
            log("Failed to launch Electron shell!", withError = True)
