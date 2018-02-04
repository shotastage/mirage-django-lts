import os
from djconsole         import project
from djconsole.flow    import Workflow
from djconsole.command import log


class DjangoDebugServerWorkFlow(Workflow):
    def main(self):
        log("Runnng server...")

        if project.in_project():
            try:
                os.system("python manage.py runserver")
            except KeyboardInterrupt:
                log("Good bye!")
        else:
            log("Failed to launch server!", withError = True, errorDetail = "You are now out of Django project.")
