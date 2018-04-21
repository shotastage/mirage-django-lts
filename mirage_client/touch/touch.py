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

import traceback
from mirage.flow import Workflow
from mirage.miragefile.conf import Config, Category, Detail
from mirage import system as mys
from . import copyright_source


class TouchWorkFlow(Workflow):

    def constructor(self):

        self._fname = self._option

        if self._fname == None:
            self._fname = mys.log("File Name", withInput = True)


    def main(self):

        try:
            proj_name = Config().get(Category.project_basic, Detail.project_name)
        except:
            proj_name = mys.log("What's the project name?", withInput = True)

        try:
            your_name = Config("secret").get(Category.private_profile, Detail.private_name)
        except:
            your_name = mys.log("What's your name?", withInput = True)

        try:
            start_year = Config().get(Category.copyright, Detail.copyright_start_year)
        except:
            start_year = mys.log("Start year", withInput = True)

        try:
            copyrights = Config().get(Category.copyright, Detail.copyright_copyrigtors)
        except:
            copyrights = mys.log("Copyrights", withInput = True)

        try:
            licensename = Config().get(Category.project_basic, Detail.project_license)
        except:
            licensename = mys.log("License name", withInput = True)

        try:
            license_url = Config("secret").get(Category.private_profile, Detail.private_license_url)
        except:
            license_url = mys.log("License doc URL", withInput = True)


        try:
            with open(str(self._fname), "w") as f:

                # When copyrights is list, copyright_source raises TypeError: unhashable type: 'list'
                if [ext for ext in [".py", ".rb", ".sh"] if ext in self._fname]:
                    f.write(
                        copyright_source.copyright_script_style_doc(proj_name, self._fname, your_name,
                                                   start_year, tuple(copyrights), licensename, license_url)
                    )
                elif [ext for ext in [".scss", ".js", ".ts", ".swift", ".c"] if ext in self._fname]:
                    f.write(
                        copyright_source.copyright_c_style_doc(proj_name, self._fname, your_name,
                                                   start_year, tuple(copyrights), licensename, license_url)
                    )

        except:
            mys.log("Failed to touch new python script \"" + self._fname + "\"!", withError = True, errorDetail = mys.raise_error_message(self.main, traceback.format_exc()))

        return True
