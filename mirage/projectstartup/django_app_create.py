# -*- coding: utf-8 -*-
"""
Copyright 2017-2020 Shota Shimazu.

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
from mirage import system as mys
from mirage.template import readme_md, gitignore
from mirage.miragefile import source


class StartupWorkFlow(Workflow):

    def constructor(self):
        self._js_runtime = self._option


    def main(self):

        # Check
        try:
            self._check_before()
        except:
            return

        # Input information
        mys.log("Please type your new Django application information.")

        # Check namespace
        try:
            self._project_name = mys.log("Project name", withInput = True)
            self._check_namesapce(self._project_name)
        except:
            mys.log("Project \"{0}\" is already exists.".format(self._project_name), withError = True,
                    errorDetail = "Please remove duplication of Django project namespace.")
            return

        version      = mys.log("App version", withInput = True, default = "0.0.1")
        author       = mys.log("Author name", withInput = True)
        email        = mys.log("Email",       withInput = True)
        git_url      = mys.log("Git URL",     withInput = True)
        license_name = mys.log("License",     withInput = True)
        description  = mys.log("Description", withInput = True)
        copyrightor  = mys.log("Copyrightor", withInput = True, default = author)




        self._create_new_django_app()

        # Create logging instance
        logger = mys.Progress()

        with proj.InDir("./" + self._project_name):

            # Generate .gitignore
            #log("Generating gitignore...")
            logger.write("Generating gitignore...", withLazy = True)
            self._create_template_git_project()

            # Generate README.md
            logger.update("Generating readme...", withLazy = True)
            self._create_docs(description)

            # Generate Miragefile
            logger.update("Generating Miragefile...", withLazy = True)
            self._create_miragefile(version, author, email, git_url, license_name, description, copyrightor)

            # Add remote repo
            logger.update("Adding remote repository...", withLazy = True)
            mys.command("git remote add origin " + git_url)

        # Completed
        logger.update("Completed!")


    def _create_new_django_app(self):
        mys.command("django-admin startproject " + self._project_name)


    def _create_miragefile(self, version, author, email, git_url, license_name, description, copyrightors):
        with open("Miragefile", "w") as f:
            f.write(source.create(self._project_name, version, author, email, git_url, license_name, description, copyrightors))

    def _create_template_git_project(self):
        ignorance = gitignore.src()

        with open(".gitignore", "w") as f:
            f.write(ignorance)

        mys.command("git init")


    def _create_docs(self, description):
        with open("README.md", "a") as readme:
            readme.write(readme_md.src(self._project_name, description))


    def _check_before(self):

        try:
            import django
        except ImportError:
            mys.log("Failed to import Django!", withError = True,
                                errorDetail = "You have to install Django before creating a new Django project.")
            raise ImportError


    def _check_namesapce(self, name):
        if os.path.exists(name):
            raise FileExistsError
