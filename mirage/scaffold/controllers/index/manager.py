from flask import Flask, render_template

from mirage import project
from mirage.scaffold.manager import ScaffoldManager
from mirage.scaffold import configure
from mirage.miragefile import utils
from ... import iyashi


class IndexManager(ScaffoldManager):
    
    @staticmethod
    def make_view():
        if utils.get_reserved_addon_config("iyashi"):
            iyashi_image = iyashi.select_photo()
        else:
            iyashi_image = "none"

        return render_template('index.html',
            project_name = project.get_project_name(),
            app_list = project.get_app_list(),
            iyashi_image    = iyashi_image
        )
