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

from mirage import system
from mirage.miragefile import utils
from mirage.proj import environ
from mirage.flow import Workflow
from .templates import procfile, runtime


class DjangoHerokuConfigureWorkFlow(Workflow):

    def main(self):
        system.log("Creating heroku configurations...")
        self._create_heroku_configuation()


    def _create_heroku_configuation(self):
        with open("Procfile", "w") as pf:
            pf.write(procfile.src(
                str(utils.get_django(utils.MiragefileDataCategory.django_module))
            ))
        with open("runtime.txt", "w") as rf:
            rf.write(runtime.src())
