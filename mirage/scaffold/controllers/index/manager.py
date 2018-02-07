from flask import Flask, render_template

from djconsole import project
from djconsole.scaffold.manager import ScaffoldManager
from djconsole.scaffold import configure
from ... import iyashi


class IndexManager(ScaffoldManager):
    
    @staticmethod
    def make_view():
        if configure.get_proj_config("iyashi"):
            iyashi_image = iyashi.select_photo()
        else:
            iyashi_image = "none"

        return render_template('index.html',
            project_name = project.get_project_name(),
            app_list = project.get_app_list(),
            iyashi_image    = iyashi_image
        )
