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
from mirage.command import log, raise_error_message
from mirage.miragefile.utils import MiragefileDataCategory
from mirage import miragefile
from mirage import project
from . import copyright_source


class TouchWorkFlow(Workflow):

    def additional_init_(self):
        
        self._fname = self._option
      
        if self._fname == None:
            self._fname = log("File Name", withInput = True)


    def main(self):


        proj_name   = miragefile.utils.get_project(
                                MiragefileDataCategory.project_name)

        try:
            your_name = miragefile.utils.get_private_profile("name")
        except:
            your_name = log("What's your name?", withInput = True)


        start_year  = miragefile.utils.get_copyright(
                                MiragefileDataCategory.copyright_start_year)

        copyrights  = miragefile.utils.get_copyright(
                                MiragefileDataCategory.copyright_copyrigtors)

        licensename = miragefile.utils.get_project(
                                MiragefileDataCategory.project_license)

        try:
            license_url = miragefile.utils.get_private_profile("license")
        except:
            license_url = log("License doc URL", withInput = True)


        if project.in_project():
            try:
                with open(str(self._fname), "w") as f:
                    f.write(
                        copyright_source.copyright_doc(proj_name, self._fname, your_name,
                                                            start_year, copyrights, licensename, license_url)
                    )
            except:
                log("Failed to touch new python script!", withError = True, errorDetail = raise_error_message(self.main))
        else:
            log("Failed to launch server!", withError = True, errorDetail = "You are now out of Django project.")
