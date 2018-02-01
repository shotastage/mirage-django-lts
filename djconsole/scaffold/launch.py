import subprocess
import webbrowser
from djconsole.flow import Workflow
from djconsole.command import log, raise_error_message
from djconsole.scaffold import server
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
            sleep(1)
            webbrowser.open("http://127.0.0.1:5000")
        except:
            log("Failed to launch Electron shell!", withError = True)
