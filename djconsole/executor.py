# -*- coding: utf-8 -*-
"""
Copyright 2017 Shota Shimazu.

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

from djconsole.flow                                     import GatheredArgs
from djconsole.projectstartup.django_app_create         import DjangoStartupFlow
from djconsole.cms_projectstartup.django_cms_create     import DjangoCMSStartupFlow
from djconsole.generate.app                             import DjangoAppMakeFlow
from djconsole.console.django_console                   import DjangoConsoleFlow
from djconsole.destroy.destroy                          import DjangoDestroyFlow
from djconsole.git.git                                  import DjangoGitFlow
from djconsole.dammy.dammy                              import DjangoDammyFlow
from djconsole.command                                  import log, reserve_as_command

from djconsole.options      import DjConsoleOptions as djops
from djconsole.generate     import app
from djconsole.generate     import model
from djconsole.server       import debug_server



def exe(action, action_type, args):
    action_handler = GatheredArgs(action, action_type, args)

    new(action_handler, action)
    cms_new(action_handler, action)
    generate(action_handler, action)
    server(action_handler, action)
    console(action_handler, action)
    destroy(action_handler, action)
    git(action_handler, action)
    dammy(action_handler, action)


@reserve_as_command("new")
def new(handler, action):
    try:
        dj_new_flow = DjangoStartupFlow(handler._action_target)
        dj_new_flow.execute()
    except:
        dj_new_flow = DjangoStartupFlow()
        dj_new_flow.execute()


@reserve_as_command("new:cms", "nc")
def cms_new(handler, action):
    try:
        dj_cms_new_flow = DjangoCMSStartupFlow(handler._action_target)
        dj_cms_new_flow.execute()
    except:
        dj_cms_new_flow = DjangoCMSStartupFlow()
        dj_cms_new_flow.execute()


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


@reserve_as_command("destroy")
def destroy(handler, action):
    try:
        dj_destroy_flow = DjangoDestroyFlow(handler._action_target, handler.args)
        dj_destroy_flow.execute()
    except:
        pass


@reserve_as_command("git")
def git(handler, action):
    try:
        dj_git_flow = DjangoGitFlow(handler._action_target)
        dj_git_flow.execute()
    except:
        pass


@reserve_as_command("dammy")
def dammy(handler, action):
    try:
        dj_dammy_flow = DjangoDammyFlow(handler._action_target)
        dj_dammy_flow.execute()
    except:
        pass
