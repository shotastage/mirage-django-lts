from console import log
from options import DjConsoleOptions as djops
from projectstartup.django_app_create import dj_new_flow
from generate import app


def exe(action, args):
    
    if action == djops.dj_new:

        """
         If the args value not provided.
        """
        try:
            dj_new_flow(args[0])
        except:
            dj_new_flow()

    elif action == djops.dj_gen:
        _gen(args[0])

    else:
        pass

    

def _gen(second_arg):
    if second_arg == "app":
        try:
            app.dj_app_flow()
        except:
            log("Failed to excute app generation!", withError = True)
