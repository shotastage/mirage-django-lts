# -*- coding: utf-8 -*-
"""
Copyright 2017 Shota Shimazu.

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

from shutil import move
from djconsole.flow import Flow
from djconsole.command import log, command
from djconsole.cms_projectstartup.readme import create_readme_doc



class DjangoCMSStartupFlow(Flow):

    def __init__(self, name = None):
        self._project_name = name

    def flow(self):

        if self._project_name == None:
            log("Please type your new Django CMS application name.")
            self._project_name = log("Django CMS name", withInput = True)

        try:
            self._check(self._project_name)
        except:
            log("Project {0} is already exists.".format(self._project_name), withError = True)

        
        self._create_new_django_app(self._project_name)

        current = os.getcwd()
        os.chdir("./" + self._project_name)
        self._create_template_git_project(self._project_name)
        self._create_docs(self._project_name)
        os.chdir("../")


    def _create_new_django_app(self, name):
        log("Creating Django CMS application...")
        log("Please wait for a moment.")
        command("djangocms " + name)


    def _create_template_git_project(self, name):
        command("curl -O https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore")
        move("Python.gitignore", ".gitignore")
        command("git init")

    def _create_docs(self, name):
        with open("README.md", "a") as readme:
            readme.write(create_readme_doc(name))


    def _check(self, name):
        if os.path.exists(name):
            raise FileExistsError
