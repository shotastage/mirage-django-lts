import sys

from flask import Flask, render_template

from djconsole.flow import Workflow
from djconsole      import project


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html',
        project_name = project.get_project_name()
    )

class ScaffoldServerWorkflow(Workflow):

    def main(self):
        app.run()
