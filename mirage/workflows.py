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

from mirage.console.django_console import DjangoConsoleWorkFlow, DjangoDBConsoleWorkFlow
class DjangoConsole(DjangoConsoleWorkFlow): pass
class DjangoDBConsole(DjangoDBConsoleWorkFlow): pass


from mirage.projectstartup.react_app_create import ReactStartupWorkFlow
class ReactStartup(ReactStartupWorkFlow): pass

from mirage.projectstartup.django_app_create import StartupWorkFlow
class Startup(StartupWorkFlow): pass

from mirage.help.usage_flow import UsageShowWorkFlow, VersionShowWorkFlow
class UsageShow(UsageShowWorkFlow): pass
class VersionShow(VersionShowWorkFlow): pass

from mirage.db.migrate import DjangoMigrateWorkFlow
class DjangoMigrate(DjangoMigrateWorkFlow): pass

from mirage.db.reset import DjangoDBResetWorkFlow
class DjangoDBReset(DjangoDBResetWorkFlow): pass

from mirage.generate.app import DjangoAppMakeWorkFlow
class DjangoAppMake(DjangoAppMakeWorkFlow): pass

from mirage.backup.backup import DjangoBackupAppWorkFlow
class DjangoBackupApp(DjangoBackupAppWorkFlow): pass

from mirage.configure.configure import ConfigureWorkFlow
class Configure(ConfigureWorkFlow): pass

from mirage.destroy.destroy import DjangoDestroyWorkFlow
class DjangoDestroy(DjangoDestroyWorkFlow): pass

from mirage.server.debug_server import DjangoDebugServerWorkFlow
class DjangoDebugServer(DjangoDebugServerWorkFlow): pass

from mirage.generate.model import DjangoModelMakeWorkflow
class DjangoModelMake(DjangoModelMakeWorkflow): pass

from mirage.heroku.configure import DjangoHerokuConfigureWorkFlow
class DjangoHerokuConfigure(DjangoHerokuConfigureWorkFlow): pass

from mirage.server.debug_server import DjangoLaunchBrowserWorkflow
class DjangoLaunchBrowser(DjangoLaunchBrowserWorkflow): pass

from mirage.manage.executor import DjangoManagePyWorkflow
class DjangoManagePy(DjangoManagePyWorkflow): pass

from mirage.db.merge import DjangoMergeMigrationWorkFlow
class DjangoMergeMigration(DjangoMergeMigrationWorkFlow): pass

from mirage.transfer.transfer import MirageTransferWorkflow
class MirageTransfer(MirageTransferWorkflow): pass


###########################################################
# ALL IMPORT                                              #
###########################################################

from mirage.projectstartup.minimum_app_create import *

from mirage.confscript import *

from mirage.generate import *

from mirage.checker import *

from mirage.projectstartup import *

