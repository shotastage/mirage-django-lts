import os
import webbrowser
from mirage import proj
from mirage.flow import Workflow
from mirage.flow_next import WorkflowNext
from mirage import system as mys


class DjangoDebugServerWorkFlow(Workflow):

    def main(self):
        with proj.MirageEnvironment(proj.MirageEnvironmentLevel.indjango):
            try:
                os.system("python manage.py runserver")
            except KeyboardInterrupt:
                mys.log("Good bye!")
            except:
                mys.log("Failed to launch web browser!", withError = True)



class DjangoLaunchBrowserWorkflow(WorkflowNext):

    def __init__(self):
        self._url = self._option

    def main(self):

        if self._url == None:
            webbrowser.open("http://127.0.0.1:8000")
        else:
            webbrowser.open(self._url)
