from flask import Flask, render_template

from djconsole.flow import Workflow
from djconsole      import project

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
        project_name = project.get_project_name(),
        app_list = project.get_app_list(),
        proj_name = configure.get_proj_config("name"),
        proj_ver  = configure.get_proj_config("version"),
        proj_author  = configure.get_proj_config("author"),
        proj_git  = configure.get_proj_config("git"),
        proj_license  = configure.get_proj_config("license"),
        proj_msg  = configure.get_proj_config("description"),
        all_conf = configure.get_all_conf()
    )

    
class ScaffoldServerWorkflow(Workflow):

    def main(self):
        app.run(host='127.0.0.1', port = 5050)


if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost', port = 1234)
