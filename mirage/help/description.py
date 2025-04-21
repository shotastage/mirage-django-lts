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


[Git]

gg            pull                          Pull latest source base from remote repository.
gg            push                          Create and push current changes to remote repository.


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
q             update                        Check update.
q             system                        Check platform and Python version.

""".format(version.__version__)


def version_doc():
    return """
Mirage Version {0}

https://github.com/shotastage/django-mirage

Copyright (c) 2017-2024 Shota Shimazu
This software is licensed under the Apache v2, see LICENSE for detail.
""".format(version.__version__)
