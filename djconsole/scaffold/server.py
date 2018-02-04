import webbrowser

from flask import Flask, render_template
from djconsole import project
from djconsole.command import log, raise_error_message
from djconsole.flow import Workflow
from .controllers.index.manager import IndexManager
from .controllers.app.manager import AppManager
from .controllers.config import manager as m
from . import configure


app = Flask(__name__)


@app.route("/")
def index():
    return IndexManager.make_view()

@app.route("/app/")
def app_view():
    return AppManager.make_view()

@app.route("/config/")
def config():
    return m.ConfigManager.make_view()

@app.route("/config/django/")
def config_django():
    return m.DjangoConfigManager.make_view()


@app.route("/config/nodejs/")
def config_nodejs():
    return m.DjangoConfigManager.make_view()


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

    
class ScaffoldServerWorkflow(Workflow):
    def main(self):
        app.run(host = "127.0.0.1", port = 5050)


if __name__ == "__main__":
    log("Scaffold server for debug.")
    log("Listening started on http://127.0.0.1:1234")
    webbrowser.open("http://127.0.0.1:1234")
    app.debug = True
    app.run(host = "127.0.0.1", port = 1234)
