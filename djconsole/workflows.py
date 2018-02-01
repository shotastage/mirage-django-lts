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


from djconsole.console.django_console import DjangoConsoleWorkFlow, DjangoDBConsoleWorkFlow
class DjangoConsole(DjangoConsoleWorkFlow): pass
class DjangoDBConsole(DjangoDBConsoleWorkFlow): pass


from djconsole.projectstartup.django_app_create import DjangoStartupWorkFlow, DjangoCMSStartupWorkFlow
class DjangoStartup(DjangoStartupWorkFlow): pass
class DjangoCMSStartup(DjangoCMSStartupWorkFlow): pass


from djconsole.help.usage_flow import UsageShowWorkFlow, VersionShowWorkFlow
class UsageShow(UsageShowWorkFlow): pass
class VersionShow(VersionShowWorkFlow): pass

from djconsole.db.migrate import DjangoMigrateWorkFlow
class DjangoMigrate(DjangoMigrateWorkFlow): pass

from djconsole.db.reset import DjangoDBResetWorkFlow
class DjangoDBReset(DjangoDBResetWorkFlow): pass

from djconsole.generate.app import DjangoAppMakeWorkFlow
class DjangoAppMake(DjangoAppMakeWorkFlow): pass

from djconsole.backup.backup import DjangoBackupAppWorkFlow
class DjangoBackupApp(DjangoBackupAppWorkFlow): pass

from djconsole.configure.configure import ConfigureWorkFlow
class Configure(ConfigureWorkFlow): pass

from djconsole.destroy.destroy import DjangoDestroyWorkFlow
class DjangoDestroy(DjangoDestroyWorkFlow): pass

from djconsole.scaffold.launch import ScaffoldWorkflow
class Scaffold(ScaffoldWorkflow): pass

from djconsole.scaffold.server import ScaffoldServerWorkflow
class ScaffoldServer(ScaffoldServerWorkflow): pass
