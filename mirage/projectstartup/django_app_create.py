import os
import shutil

from mirage.flow import Flow, Workflow, Stepflow
from mirage.command import log, command
from mirage.miragefile import source
from mirage import project2
from .readme            import create_readme_doc
from .gitignore         import create_gitignore
from .package_json      import create_package_json

class DjangoStartupWorkFlow(Workflow):
    
    def additional_init_(self):
        self._project_name = None


    def main(self):
        # Check 

        try:
            self._check_before()
        except:
            return

        # Input information
        log("Please type your new Django application information.")

        # Check namespace
        try:
            self._project_name = log("Project name", withInput = True)
            self._check_namesapce(self._project_name)
        except:
            log("Project \"{0}\" is already exists.".format(self._project_name), withError = True,
                    errorDetail = "Please remove duplication of Django project namespace.")
            return

        version      = log("App version", withInput = True, default = "0.0.1")
        author       = log("Author name", withInput = True)
        email        = log("Email",       withInput = True)
        git_url      = log("Git URL",     withInput = True)
        license_name = log("License",     withInput = True)
        description  = log("Description", withInput = True)
        copyrightor  = log("Copyrightor", withInput = True, default = author)



        
        self._create_new_django_app()


        with project2.InDir("./" + self._project_name):
            
            # Generate .gitignore
            log("Generating gitignore...")
            self._create_template_git_project()

            # Generate README.md
            log("Generating readme...")
            self._create_docs()

            # Generate Miragefile
            log("Generating Miragefile...")
            self._create_miragefile(version, author, email, git_url, license_name, description, copyrightor)

            # Generate package.json
            log("Generating package configuration...")
            self._create_package_json(version, description, git_url, author, email, license_name)

            # Add remote repo
            log("Adding remote repository...")
            command("git remote add origin " + git_url)

            # Install webpack
            log("Installing assets builder...")
            command("yarn add --dev webpack")

            # Make shell directory
            os.mkdir("shell")

        # Completed
        log("Completed!")
    

    def _create_new_django_app(self):
        command("django-admin startproject " + self._project_name)


    def _create_miragefile(self, version, author, email, git_url, license_name, description, copyrightors):    
        with open("Miragefile", "w") as f:
            f.write(source.create(self._project_name, version, author, email, git_url, license_name, description, copyrightors))
     

    
    def _create_package_json(self, version, description, git_repository, author_name, email, license_name):
        with open("package.json", "w") as f:
            data = create_package_json(self._project_name, version, description, git_repository, author_name, email, license_name)
            f.write(data)


    def _create_template_git_project(self):
        ignorance = create_gitignore()

        with open(".gitignore", "w") as f:
            f.write(ignorance)

        command("git init")


    def _create_docs(self):
        with open("README.md", "a") as readme:
            readme.write(create_readme_doc(self._project_name))


    def _check_before(self):
        
        try:
            import django
        except ImportError:
            log("Failed to import Django!", withError = True,
                                errorDetail = "You have to install Django before creating a new Django project.")
            raise ImportError


    def _check_namesapce(self, name):
        if os.path.exists(name):
            raise FileExistsError


class DjangoCMSStartupWorkFlow(Workflow):

    def additional_init_(self):
        try:
            self._project_name = self._option
        except:
            self._project_name = None


    def main(self):

        if self._project_name == None:
            log("Please type your new Django CMS application name.")
            self._project_name = log("Django CMS name", withInput = True)

        try:
            self._check(self._project_name)
        except:
            log("Project {0} is already exists.".format(self._project_name), withError = True)

        
        self._create_new_django_app(self._project_name)

        with project2.InDir("./" + self._project_name):
            self._create_template_git_project(self._project_name)
            self._create_docs(self._project_name)


    def _create_new_django_app(self, name):
        log("Creating Django CMS application...")
        log("Please wait for a moment.")
        command("djangocms " + name)


    def _create_template_git_project(self, name):
        ignorance = create_gitignore()

        with open(".gitignore", "w") as f:
            f.write(ignorance)

        command("git init")


    def _create_docs(self, name):
        with open("README.md", "a") as readme:
            readme.write(create_readme_doc(name))


    def _check(self, name):
        if os.path.exists(name):
            raise FileExistsError
