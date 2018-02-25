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
from mirage.miragefile.conf import Config, Category, Detail
from mirage import project
from mirage import system as mys

from . import copyright_source


class TouchWorkFlow(Workflow):

    def additional_init_(self):
        
        self._fname = self._option
      
        if self._fname == None:
            self._fname = mys.log("File Name", withInput = True)


    def main(self):

        proj_name = Config().get(Category.project_basic, Detail.project_name)

        try:
            your_name = Config("secret").get(Category.private_profile, Detail.private_name)
        except:
            your_name = mys.log("What's your name?", withInput = True)


        start_year = Config().get(Category.copyright, Detail.copyright_start_year)

        copyrights = Config().get(Category.copyright, Detail.copyright_copyrigtors)

        licensename = Config().get(Category.project_basic, Detail.project_license)

        try:
            license_url = Config("secret").get(Category.private_profile, Detail.private_license_url)
        except:
            license_url = mys.log("License doc URL", withInput = True)


        try:
            with open(str(self._fname), "w") as f:
                f.write(
                    copyright_source.copyright_doc(proj_name, self._fname, your_name,
                                                            start_year, copyrights, licensename, license_url)
                )
        except:
            mys.log("Failed to touch new python script!", withError = True, errorDetail = mys.raise_error_message(self.main))
