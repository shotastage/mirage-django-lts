from flask import Flask, render_template, request

from mirage import project
from mirage.scaffold.manager import ScaffoldManager
from mirage.scaffold import configure
from mirage.miragefile import utils as mfile
from mirage.miragefile.utils import MiragefileDataCategory as Category


class ConfigManager(ScaffoldManager):
    
    @staticmethod
    def make_view(req):
        if req.method == "GET":
            return render_template('config.html',
                project_name    = mfile.get_project(Category.project_name),
                app_list        = project.get_app_list(),
                proj_name       = mfile.get_project(Category.project_name),
                proj_ver        = mfile.get_project(Category.project_version),
                proj_author     = mfile.get_project(Category.project_author),
                proj_git        = mfile.get_project(Category.project_git),
                proj_license    = mfile.get_project(Category.project_license),
                proj_msg        = mfile.get_project(Category.project_description)
            )
        
        if req.method == "POST":
            return render_template('config.html',
                project_name    = project.get_project_name(),
                app_list        = project.get_app_list(),
                proj_name       = mfile.get_project(Category.project_name),
                proj_ver        = mfile.get_project(Category.project_version),
                proj_author     = mfile.get_project(Category.project_author),
                proj_git        = mfile.get_project(Category.project_git),
                proj_license    = mfile.get_project(Category.project_license),
                proj_msg        = mfile.get_project(Category.project_description)
            )

class DjangoConfigManager(ScaffoldManager):

    @staticmethod
    def make_view():
        return render_template('config_django.html',
            project_name    = project.get_project_name(),
            app_list        = project.get_app_list(),
            proj_name       = mfile.get_project(Category.project_name),
            proj_ver        = mfile.get_project(Category.project_version),
            proj_author     = mfile.get_project(Category.project_author),
            proj_git        = mfile.get_project(Category.project_git),
            proj_license    = mfile.get_project(Category.project_license),
            proj_msg        = mfile.get_project(Category.project_description),
        )


class NodeConfigManager(ScaffoldManager):

    @staticmethod
    def make_view():
        return render_template('config_nodejs.html',
            project_name    = project.get_project_name(),
            app_list        = project.get_app_list(),
            proj_name       = mfile.get_project(Category.project_name),
            proj_ver        = mfile.get_project(Category.project_version),
            proj_author     = mfile.get_project(Category.project_author),
            proj_git        = mfile.get_project(Category.project_git),
            proj_license    = mfile.get_project(Category.project_license),
            proj_msg        = mfile.get_project(Category.project_description),
        )
