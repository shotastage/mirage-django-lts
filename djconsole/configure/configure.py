# -*- coding: utf-8 -*-
"""
Copyright 2017-2018 Shota Shimazu.

This software is licensed under the MIT, see LICENSE for detail.
"""


import os

from djconsole          import fileable
from djconsole.flow     import Workflow
from djconsole.command  import log, raise_error_message
from djconsole.command  import command

from djconsole.projectstartup.djfile import create_djfile


class ConfigureWorkFlow(Workflow):

    def main(self):
        self._configure()

    def _configure(self):
        if fileable.exists("DjFile"):
            if log("DjFile is exists. Are you sure to overwrite DjFile?", withConfirm = True):
                os.remove("DjFile")
            else:
                log("DjFile is already exists!", withError = True)
                raise FileExistsError
                return
        
        app_name    = log("App name", withInput = True)
        version     = log("App version", withInput = True)
        author      = log("Author name", withInput = True)
        git_url     = log("Git URL", withInput = True)
        license_name = log("License", withInput = True)

        with open("DjFile", "w") as f:
            f.write(create_djfile(app_name, version, author, git_url, license_name))
    