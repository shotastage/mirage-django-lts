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

from mirage.flow import Workflow
from mirage import project
from . import copyright_source

class TouchWorkFlow(Workflow):

    def additional_init_(self):
        self._fname = None

    def main(self):

        if project.in_project():
            try:
                with open(self._fname, "w") as f:
                    f.write(copyright_source.copyright_doc())
            except:
                log("Good bye!")
        else:
            log("Failed to launch server!", withError = True, errorDetail = "You are now out of Django project.")
