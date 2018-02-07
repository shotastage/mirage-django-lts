import os
import shutil

from djconsole.flow     import Flow, Workflow, Stepflow
from djconsole.command  import log, command
from .readme            import create_readme_doc
from .gitignore         import create_gitignore
from .djfile            import create_djfile
from .package_json      import create_package_json

class DjangoStartupWorkFlow(Workflow):
    
    def additional_init_(self):
        try:
            self._project_name = self._option
        except:
            self._project_name = None


    def main(self):

        # Input information
        log("Please type your new Django application information.")

        if self._project_name == None: self._project_name = log("Project name", withInput = True)
        version      = log("App version", withInput = True, default = "0.0.1")
        author       = log("Author name", withInput = True)
        email        = log("Email",       withInput = True)
        git_url      = log("Git URL",     withInput = True)
        license_name = log("License",     withInput = True)
        description  = log("Description", withInput = True)


        try:
            self._check(self._project_name)
        except:
            log("Project {0} is already exists.".format(self._project_name), withError = True)

        
        self._create_new_django_app()

        current = os.getcwd()

        os.chdir("./" + self._project_name)

        self._create_template_git_project()
        self._create_docs()
        self._create_djfile(version, author, email, git_url, license_name, description)
        self._create_package_json(version, description, git_url, author, email, license_name)
        command("git remote add origin " + git_url)
        
        # Additional creation
        os.mkdir("shell")

        os.chdir("../")

    

    def _create_new_django_app(self):
        command("django-admin startproject " + self._project_name)


    def _create_djfile(self, version, author, email, git_url, license_name, description):
        with open("DjFile", "w") as f:
            f.write(create_djfile(self._project_name, version, author, email, git_url, license_name, description))

    
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


    def _check(self, name):
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
