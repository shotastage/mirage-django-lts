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

import tempfile, sys, traceback
from urllib import request
from mirage.proj import InDir
from mirage.flow import Workflow
from mirage.core import Void
from mirage.version import __version__ as ver
from mirage import system as mys



class UpdateCheckFlow(Workflow):

    def constructor(self) -> Void:
        self._url = "https://raw.githubusercontent.com/shotastage/mirage-django-lts/master/mirage/version.py"


    def main(self) -> Void:
        mys.log("Checking mirage update...")

        with tempfile.TemporaryDirectory() as td:
            with InDir(td):
                sys.path.append(td)
                request.urlretrieve(self._url, "mg_version_check.py")

                try:
                    import mg_version_check
                except ImportError:
                    mys.log("Failed to get version information!", withError=True,
                            errorDetail=mys.raise_error_message(self.main, traceback.format_exc()))
                    return

                if ver == mg_version_check.__version__:
                    if ver == "0.1.9":
                        mys.log("New mirage framework tools available!")
                        mys.log("See, https://github.com/shotastage/mirage-django for detail.")

                        mys.log("LTS Update available!", withError=True)
                        print("This version: {0}".format(ver))
                        print("Available version: {0}".format(mg_version_check.__version__))
                else:
                    mys.log("LTS Update available!", withError=True)
                    print("This version: {0}".format(ver))
                    print("Available version: {0}".format(mg_version_check.__version__))
