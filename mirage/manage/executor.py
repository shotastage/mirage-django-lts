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
from mirage import proj
from mirage.flow import Workflow

class DjangoCreateSuperUserWorkflow(Workflow):

    def main(self):
        with proj.MirageEnvironment(proj.MirageEnvironmentLevel.indjango):
            os.system("python manage.py createsuperuser")


class DjangoManagePyWorkflow(Workflow):

    def constructor(self):
        self._cmd = self._option

    def main(self):
        
        if self._cmd == "superuser":
            self.createsuperuser()
        else:
            self.excute_manage_cmd()


    def createsuperuser(self):
        self._cmd = "createsuperuser"
        self.excute_manage_cmd()


    def excute_manage_cmd(self):
        with proj.MirageEnvironment(proj.MirageEnvironmentLevel.indjango):
            os.system("python manage.py " + self._cmd)
