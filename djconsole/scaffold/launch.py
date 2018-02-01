import os
import shlex
import subprocess
import webbrowser
import threading

from time import sleep

from djconsole.flow     import Workflow
from djconsole.command  import log, raise_error_message
from djconsole.scaffold import server


class ScaffoldWorkflow(Workflow):
    
    def main(self):
        server = None

        log("Launching server...")
       

        try:
            try:
                devnull = open('/dev/null', 'w')
                server = subprocess.Popen(shlex.split("djc internal_server_launch"), stdout=devnull, stderr=devnull)
            except:
                log("Failed to launch server!", withError = True)

            log("Launching shell...")
            log("Ctl + C to exit scaffold.")
            sleep(1)
            webbrowser.open("http://127.0.0.1:5000")
            server.wait()
    
        except KeyboardInterrupt:
            server.kill()
