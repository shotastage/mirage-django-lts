import sys

from flask import Flask, render_template

from djconsole.flow import Workflow
from djconsole      import project


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html',
        project_name = project.get_project_name(),
        app_list = ["sample", "upload", "show", "api"]
    )

    
class ScaffoldServerWorkflow(Workflow):

    def main(self):
        app.run()


if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost', port=18463)
