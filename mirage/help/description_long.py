from mirage import version

def usage_doc():
    return """
Mirage v{0}

Usage:
    mg [action] option <--sub-option> <inputs>

    mg [action]:[subaction] option <--sub-option> <inputs>


Commands:              Short:       Options:                      Descriptions:

    newproject         new                                        Create a new Django project.
    newproject:react   new:react                                  Create a new Django API project with React.js front-end.
    backup             b            app         <app name>        Backup exsiting app.
    launch-browser     browser                  <URL>             Launch browser set as default by system.
    configure          conf                     <config type>     Generate miragefile or reconfig mirage.
    console            c                                          Launch Django Python shell.
    console:db         c:db                                       Launch databse shell.
    database:migrate   db:migrate                                 Make migrations and apply migrations.
    database:merge     db:merge                                   Discard & recreate migrations.
    database:reset     db:reset                                   Reset all database. ( Only debugging SQLite is supported. )
    generate           g            app         <app names...>    Create multiple Django apps at once.
    generate           g            model       <model class>     Create Django model class.
    generate           g            module      <module bane>     Create a new Python module with __init__.py
    git                gg           pull                          Pull latest source base from remote repository.
    git                gg           push                          Create and push current changes to remote repository.
    heroku             heroku       configure                     Configure setting files for deploing to heroku.
    manage             m            test                          Run test of Django application.
    manage             m            superuser                     Create super user for Django admin.
    manage             m            <manage.py command>           Run manage.py command.
    server             s                                          Launch debugging server.
    file               f                                          Create a new Python source file with copyrights doc string.

    help               h                                          Show usage of Mirage.
    version            v                                          Print version information.
    inquiry            q            update                        Check update.
    inquiry            q            system                        Check platform and Python version.


""".format(version.__version__)


def version_doc():
    return """
Mirage Version {0}

https://github.com/shotastage/django-mirage

Copyright (c) 2017-2018 Shota Shimazu
This software is licensed under the Apache v2, see LICENSE for detail.
""".format(version.__version__)
