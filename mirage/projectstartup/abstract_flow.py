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
import datetime
from functools import lru_cache
from mirage import proj
from mirage import fileable
from mirage.flow import Workflow
from mirage import system as mys
from mirage.template import readme_md, gitignore
from mirage.miragefile import source, source2, source_secret
from mirage.template import licenses


class NgStartupWorkFlow(Workflow):

    def constructor(self):
        self._plugins = self._option


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
        license_url  = mys.log("License Url", withInput = True)
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
            self._create_docs(author, description, license_name)

            # Generate Miragefile
            logger.update("Generating Miragefile...", withLazy = True)
            self._create_miragefile(version, author, email, git_url,
                                    license_name, license_url, description, copyrightor)

            # Add remote repo
            logger.update("Adding remote repository...", withLazy = True)
            mys.command("git remote add origin " + git_url)

            # Create React App
            self._create_package_json()
            logger.update("Preparing Angular setup tools...", withLazy=True)
            logger.update("Preparing Angular setup tools... ( please wait for a momenet )")
            mys.command("yarn add --dev @angular/cli")

            # To avoid ng inside the project error, remove package.package.json
            os.remove("package.json")

            logger.update("Configuring Angular setup tools to use Yarn package...")
            mys.command("./node_modules/.bin/ng set --global packageManager=yarn")
            logger.update("Creating Angular app...", withLazy = True)
            logger.update("Creating Angular app... ( please wait for a momenet )")
            mys.command("./node_modules/.bin/ng new shell")


            if self._plugins == "--nebular":
                logger.update("Installing Nebular packages...", withLazy = True)
                logger.update("Installing Nebular packages... ( please wait for a momenet )")
                with proj.InDir("./shell"):
                    mys.command("yarn add @nebular/theme @nebular/auth")

            elif self._plugins == "--material":
                logger.update("Installing material theme packages...")
                with proj.InDir("./shell"):
                    mys.command("yarn add @angular/material @angular/cdk")

            elif self._plugins == "--bootstrap":
                logger.update("Installing Bootstrap theme packages...")
                with proj.InDir("./shell"):
                    mys.command("yarn add ngx-bootstrap")


            # Cleaning
            logger.update("Cleaning...", withLazy = True)
            fileable.rm("yarn.lock")
            fileable.rm("package.json")
            fileable.rm("node_modules/")

            with proj.InDir("./shell"):
                fileable.rm(".gitignore")
                fileable.rm("README.md")


        # Completed
        logger.update("Completed!")


    def _create_new_django_app(self):
        mys.command("django-admin startproject " + self._project_name)


    def _create_miragefile(self, version, author, email, git_url, license_name, license_url, description, copyrightors):
        with open("Miragefile", "w") as f:
            f.write(source.create(self._project_name, version, author, email, git_url, license_name, description, copyrightors))

        with open("Miragefile@next.py", "w") as f:
            f.write(source2.create(self._project_name, version, author, email, git_url, license_name, description, copyrightors))

        with open("Miragefile.secret", "w") as f:
            f.write(source_secret.create(author, email, license_url))


    def _create_package_json(self):
        with open("package.json", "w") as f:
            f.write('{"name": "tmpapp", "version": "0.0.1"}')


    def _create_template_git_project(self):
        ignorance = gitignore.src()

        with open(".gitignore", "w") as f:
            f.write(ignorance)

        mys.command("git init")


    def _create_docs(self, author, description, license_name):

        with open("README.md", "a") as readme:
            readme.write(readme_md.src(self._project_name, description))

        with open("LICENSE", "w") as doc:
            if [doc for doc in ["mit", "MIT"] if doc in license_name]:
                doc.write(licenses.mit.src(self._get_current, author))

            elif [doc for doc in ["agpl", "AGPL", "AGPLv3"] if doc in license_name]:
                doc.write(licenses.agpl_v3.src(self._get_current, author))

            elif [doc for doc in ["apache", "Apache", "Apache2"] if doc in license_name]:
                doc.write(licenses.apache_v2.src(self._get_current, author))

            elif [doc for doc in ["gpl", "GPL", "GPLv3"] if doc in license_name]:
                doc.write(licenses.gpl_v3.src(self._get_current, author))

            elif [doc for doc in ["lgpl", "LGPL", "LGPLv3"] if doc in license_name]:
                doc.write(licenses.lgpl_v3.src(self._get_current, author))

            elif [doc for doc in ["mpl", "MPL", "MPLv2"] if doc in license_name]:
                doc.write(licenses.mpl_v2.src(self._get_current, author))

            elif [doc for doc in ["unlicense", "Unlicense"] if doc in license_name]:
                doc.write(licenses.unlicense.src(self._get_current, author))



    @lru_cache(maxsize = 10)
    def _get_current(self) -> str:
        return datetime.datetime.now().strftime("%Y/%m/%d")


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
