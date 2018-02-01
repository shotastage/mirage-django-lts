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


from djconsole.command import log
from djconsole.flow import Flow, Workflow
from djconsole.destroy import app
from djconsole.project import isproject




class DjangoDestroyWorkFlow(Workflow):    

    def additional_init_(self):
        self._must_target = "app"
        self._must_destroy = self._values
    

    def main(self):
        if str(self._must_target) == "app":
            if isproject: self._destroy_app()
        else:
            log("No destroy strategy for " + str(self._must_target) + ".", withError = True)

    def _destroy_app(self):
        log("Destroying app...")
        app._backup(self._must_destroy)
        app._destroy(self._must_destroy)


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
