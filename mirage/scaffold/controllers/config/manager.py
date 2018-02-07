from flask import Flask, render_template, request

from djconsole import project
from djconsole.scaffold.manager import ScaffoldManager
from djconsole.scaffold import configure


class ConfigManager(ScaffoldManager):
    
    @staticmethod
    def make_view(req):
        if req.method == "GET":
            return render_template('config.html',
                project_name    = project.get_project_name(),
                app_list        = project.get_app_list(),
                proj_name       = configure.get_proj_config("name"),
                proj_ver        = configure.get_proj_config("version"),
                proj_author     = configure.get_proj_config("author"),
                proj_git        = configure.get_proj_config("git"),
                proj_license    = configure.get_proj_config("license"),
                proj_msg        = configure.get_proj_config("description")
            )
        
        if req.method == "POST":
            return render_template('config.html',
                project_name    = project.get_project_name(),
                app_list        = project.get_app_list(),
                proj_name       = configure.get_proj_config("name"),
                proj_ver        = configure.get_proj_config("version"),
                proj_author     = configure.get_proj_config("author"),
                proj_git        = configure.get_proj_config("git"),
                proj_license    = configure.get_proj_config("license"),
                proj_msg        = configure.get_proj_config("description")
            )

class DjangoConfigManager(ScaffoldManager):

    @staticmethod
    def make_view():
        return render_template('config_django.html',
            project_name    = project.get_project_name(),
            app_list        = project.get_app_list(),
            proj_name       = configure.get_proj_config("name"),
            proj_ver        = configure.get_proj_config("version"),
            proj_author     = configure.get_proj_config("author"),
            proj_git        = configure.get_proj_config("git"),
            proj_license    = configure.get_proj_config("license"),
            proj_msg        = configure.get_proj_config("description"),
        )


class NodeConfigManager(ScaffoldManager):

    @staticmethod
    def make_view():
        return render_template('config_nodejs.html',
            project_name    = project.get_project_name(),
            app_list        = project.get_app_list(),
            proj_name       = configure.get_proj_config("name"),
            proj_ver        = configure.get_proj_config("version"),
            proj_author     = configure.get_proj_config("author"),
            proj_git        = configure.get_proj_config("git"),
            proj_license    = configure.get_proj_config("license"),
            proj_msg        = configure.get_proj_config("description")
        )
