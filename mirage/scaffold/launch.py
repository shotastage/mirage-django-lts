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

import os
import time
import shlex
import subprocess
import webbrowser

from mirage.flow     import Workflow
from mirage.command  import log, raise_error_message
from . import server
from . import configure


class ScaffoldWorkflow(Workflow):
    
    def main(self):
        server = None

        log("Launching server...")
       
        try:
            django_path = configure.get_django_config("path")
            os.chdir(django_path)
        except:
            log("Failed to move Django project directory.", withError = True,
                errorDetail = "Config directory: " + str(os.getcwd()) + "/" + configure.get_django_config("path"))
            return

        try:
            try:
                devnull = open('/dev/null', 'w')
                server = subprocess.Popen(shlex.split("djc internal_server_launch"), stdout=devnull, stderr=devnull)
            except:
                log("Failed to launch server!", withError = True)

            log("Launching shell...")
            log("Server listening started on http://127.0.0.1:5050")
            log("Ctl + C to exit scaffold.")
            time.sleep(1)
            webbrowser.open("http://127.0.0.1:5050")
            server.wait()
    
        except KeyboardInterrupt:
            server.kill()
