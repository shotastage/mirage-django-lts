from flask import Flask

from djconsole.flow import Workflow
app = Flask(__name__)

@app.route("/")
def index():
    return "Django Console Visual Scaffold"

class ScaffoldServerWorkflow(Workflow):

    def main(self):
        app.run()
