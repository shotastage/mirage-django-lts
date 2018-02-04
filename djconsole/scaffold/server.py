import webbrowser

from flask import Flask, render_template

from djconsole.scaffold.app_manager.manager import AppManager
from djconsole.scaffold.config_manager.manager import ConfigManager


from djconsole      import project
from djconsole.command import log, raise_error_message
from djconsole.flow import Workflow

from djconsole.scaffold import configure
from djconsole.scaffold import iyashi


app = Flask(__name__)


@app.route("/")
def index():
    if configure.get_proj_config("iyashi"):
        iyashi_image = iyashi.select_photo()
    else:
        iyashi_image = "none"

    return render_template('index.html',
        project_name = project.get_project_name(),
        app_list = project.get_app_list(),
        iyashi_image    = iyashi_image
    )

@app.route("/app/")
def app_view():
    return AppManager.make_view()


@app.route("/config/")
def config():
    return ConfigManager.make_view()

@app.route("/config/django/")
def config_django():
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


@app.route("/config/nodejs/")
def config_nodejs():
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


    
class ScaffoldServerWorkflow(Workflow):
    def main(self):
        log("Server listening started on http://127.0.0.1:5050")
        app.run(host = "127.0.0.1", port = 5050)


if __name__ == "__main__":
    log("Scaffold server for debug.")
    log("Listening started on http://127.0.0.1:1234")
    webbrowser.open("http://127.0.0.1:1234")
    app.debug = True
    app.run(host = "127.0.0.1", port = 1234)
