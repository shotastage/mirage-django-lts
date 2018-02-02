from flask import Flask, render_template
from djconsole      import project
from djconsole.command import log, raise_error_message
from djconsole.flow import Workflow
from djconsole.scaffold import configure


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html',
        project_name = project.get_project_name(),
        app_list = project.get_app_list()
    )

@app.route("/config/")
def config():
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
        proj_msg        = configure.get_proj_config("description")
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
        app.run(host = "127.0.0.1", port = 5050)


if __name__ == "__main__":
    log("Scaffold server for debug.")
    app.debug = True
    app.run(host = "127.0.0.1", port = 1234)
