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

from mirage import version

def usage_doc():
    return """
Mirage v{0}

Usage:
    mg [action] option <--sub-option> <inputs>

    mg [action]:[subaction] option <--sub-option> <inputs>



[Create Project]

new                                         Create a new Django project.
new:react                                   Create a new Django API project with React.js front-end.
new:ng                                      Create a new Django API project with Angular.
                         --nebular          Create a new Angular project with Nebular.
                         --material         Create a new Angular project with Material theme.

[Utilities]

b             app         <app name>        Backup exsiting app.
browser                   <URL>             Launch browser set as default by system.
conf                      <config type>     Generate miragefile or reconfig mirage.
f                                           Create a new Python source file with copyrights doc string.


[Console]

c                                           Launch Django Python shell.
c:db                                        Launch databse shell.


[Database]

db:migrate                                  Make migrations and apply migrations.
db:merge                                    Discard & recreate migrations.
db:reset                                    Reset all database. ( Only debugging SQLite is supported. )


[Generator]

g             app         <app names...>    Create multiple Django apps at once.
g             model       <model class>     Create Django model class.
g             module      <module bane>     Create a new Python module with __init__.py


[Heroku]

heroku        configure                     Configure setting files for deploing to heroku.


[Management]

m             test                          Run test of Django application.
m             superuser                     Create super user for Django admin.
m             <manage.py command>           Run manage.py command.


[Server]

s                                           Launch debugging server.


[Help]

h                                           Show usage of Mirage.
v                                           Print version information.
?             update                        Check update.
?             system                        Check platform and Python version.

""".format(version.__version__)


def version_doc():
    return """
Mirage Version {0}

https://github.com/shotastage/django-mirage

Copyright (c) 2017-2018 Shota Shimazu
This software is licensed under the Apache v2, see LICENSE for detail.
""".format(version.__version__)
