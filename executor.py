from options import DjConsoleOptions as djops

from projectstartup.django_app_create import dj_new_flow


def exe(action, args):
    
    if action == djops.dj_new:

        """
         If the args value not provided.
        """
        try:
            dj_new_flow(args[0])
        except:
            dj_new_flow()
