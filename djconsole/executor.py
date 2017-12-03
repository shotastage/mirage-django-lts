from djconsole.flow import GatheredArgs
from djconsole.projectstartup.django_app_create import DjangoStartupFlow
from djconsole.generate.app import DjangoAppMakeFlow
from djconsole.console.django_console import DjangoConsoleFlow
from djconsole.command import log, reserve_as_command

from djconsole.options import DjConsoleOptions as djops
from djconsole.generate import app
from djconsole.generate import model
from djconsole.server import debug_server



def exe(action, action_type, args):
    action_handler = GatheredArgs(action, action_type, args)

    new(action_handler, action)
    generate(action_handler, action)
    server(action_handler, action)
    console(action_handler, action)


@reserve_as_command("new")
def new(handler, action):
    try:
        dj_new_flow = DjangoStartupFlow(handler._action_target)
        dj_new_flow.execute()
    except:
        dj_new_flow = DjangoStartupFlow()
        dj_new_flow.execute()


@reserve_as_command("generate", "g")
def generate(handler, action):
    if handler.args == None:
        return

    if handler._action_target == "app":
        try:
            dj_app_flow = DjangoAppMakeFlow(handler.args)
            dj_app_flow.execute()
        except:
            log("Failed to generate app!", withError = True)

    elif handler._action_target == "model":
        try:
            model.dj_model_flow(handler.args)
        except:
            log("Failed to generate model!", withError = True)

    else:
        log("Strategy of " + handler._action_target + " is not provided!", withError = True)


@reserve_as_command("server", "s")
def server(handler, action):
    debug_server.launch_server()



@reserve_as_command("console", "c")
def console(handler, action):
    try:
        dj_console_flow = DjangoConsoleFlow()
        dj_console_flow.execute()
    except:
        pass
