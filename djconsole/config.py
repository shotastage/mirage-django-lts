import yaml
import os
from djconsole import project


class DjConfig():

    def __init__(self):
        self._config = None
        self._load()


    def _load(self):
        if project.in_app():
            os.chdir("../")

        if project.in_project():
            with open("DjFile") as conf:
                self._config = yaml.load(conf)
