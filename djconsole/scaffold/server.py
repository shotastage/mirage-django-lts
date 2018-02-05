# -*- coding: utf-8 -*-
"""
Copyright 2017-2018 Shota Shimazu.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import webbrowser

from flask import Flask, render_template, request
from djconsole import project
from djconsole.command import log, raise_error_message
from djconsole.flow import Workflow
from .controllers.index.manager import IndexManager
from .controllers.app.manager import AppManager
from .controllers.config.manager import ConfigManager, DjangoConfigManager, NodeConfigManager
from . import configure


app = Flask(__name__)


@app.route("/")
def index():
    return IndexManager.make_view()

@app.route("/app/")
def app_view():
    return AppManager.make_view()

@app.route("/config/", methods=["GET", "POST"])
def config():
    return ConfigManager.make_view(request)

@app.route("/config/django/")
def config_django():
    return DjangoConfigManager.make_view()


@app.route("/config/nodejs/")
def config_nodejs():
    return NodeConfigManager.make_view()


@app.errorhandler(404)
def dj_errorhandler(error):
    return render_template("error.html", error_status = "404")


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("error.html", error_status = "500")


class ScaffoldServerWorkflow(Workflow):
    def main(self):
        app.run(host = "127.0.0.1", port = 5050)


if __name__ == "__main__":
    log("Scaffold server for debug.")
    log("Listening started on http://127.0.0.1:1234")
    webbrowser.open("http://127.0.0.1:1234")
    app.debug = True
    app.run(host = "127.0.0.1", port = 1234)
