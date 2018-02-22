# -*- coding: utf-8 -*-
"""
Copyright 2017-2018 Shota Shimazu.

This software is licensed under the MIT, see LICENSE for detail.
"""

import os
import time
import webbrowser
from mirage         import project
from mirage.flow    import Workflow
from mirage.command import log


class DjangoDebugServerWorkFlow(Workflow):
    def main(self):
        log("Runnng server...")

        if project.in_project():
            try:
                os.system("python manage.py runserver")
                # time.sleep(1)
                # webbrowser.open("http://127.0.0.1:8000/")
            except KeyboardInterrupt:
                log("Good bye!")
        else:
            log("Failed to launch server!", withError = True, errorDetail = "You are now out of Django project.")
