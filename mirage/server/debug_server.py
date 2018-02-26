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
import webbrowser
from mirage import proj
from mirage.flow    import Workflow
from mirage import system as mys

class DjangoDebugServerWorkFlow(Workflow):
    def main(self):
        mys.log("Runnng server...")

        with proj.MirageEvironmet(proj.MirageEvironmetLevel.indjango):
       
            try:
                os.system("python manage.py runserver")
                # time.sleep(1)
                # webbrowser.open("http://127.0.0.1:8000/")
            except KeyboardInterrupt:
                mys.log("Good bye!")
            except:
                mys.log("Failed to launch server!", withError = True)
 