![Mirage](./docs/assets/logo.png)

[![Updates](https://pyup.io/repos/github/shotastage/django-mirage/shield.svg)](https://pyup.io/repos/github/shotastage/django-mirage/)
[![Python 3](https://pyup.io/repos/github/shotastage/django-mirage/python-3-shield.svg)](https://pyup.io/repos/github/shotastage/django-mirage/)
[![PyPI version](https://badge.fury.io/py/django-mirage.svg)](https://badge.fury.io/py/django-mirage)
[![PyPI](https://img.shields.io/pypi/pyversions/django-mirage.svg)]()
[![Build Status](https://travis-ci.org/shotastage/django-mirage.svg?branch=master)](https://travis-ci.org/shotastage/django-mirage)
[![GitHub release](https://img.shields.io/github/release/shotastage/django-mirage.svg)](https://github.com/shotastage/django-mirage/releases)
[![PyPI](https://img.shields.io/pypi/format/django-mirage.svg)]()
[![PyPI](https://img.shields.io/pypi/l/django-mirage.svg)](https://opensource.org/licenses/Apache-2.0)


**[mirage ~ ♪](https://youtu.be/nhrXbPlpdQQ?t=3m4s)** extended django admin or manage.py command.

# ⬇️  Installation

Installing Mirage with Pipenv is recommended.

```
pipenv install -d django-mirage
```

If you don't use `pipenv`, you can install it with pip.

```
pip install django-mirage
```

You can build this package manually.

```
make before_node
make build_all
```

# 🖥  Usage

```
Usage:
    mg [action] option <--sub-option> <inputs>

    mg [action]:[subaction] option <--sub-option> <inputs>


Actions:
    newproject         new                                      Create a new Django project.
    newproject:react   new:react                                Create a new Django API project with React.js front-end.
    newproject:ng      new:ng                                   Create a new Django API project with Angular.
                                                --nebular       Create a new Angular project with Nebular.
                                                --material      Create a new Angular project with Material theme.
    backup             b            app         <app name>      Backup exsiting app.
    launch-browser     browser                  <URL>           Launch browser set as default by system.
    configure          conf                     <config type>   Generate miragefile or reconfig mirage.
    console            c                                        Launch Django Python shell.
    console:db         c:db                                     Launch databse shell.
    database:migrate   db:migrate                               Make migrations and apply migrations.
    database:merge     db:merge                                 Discard & recreate migrations.
    database:reset     db:reset                                 Reset all database. ( Only debugging SQLite is supported. )
    generate           g            app         <app names...>  Create multiple Django apps at once.
    generate           g            model       <model class>   Create Django model class.
    generate           g            module      <module bane>   Create a new Python module with __init__.py
    heroku             heroku       configure                   Configure setting files for deploing to heroku.
    manage             m            test                        Run test of Django application.
    manage             m            superuser                   Create super user for Django admin.
    manage             m            <manage.py command>         Run manage.py command.
    scaffold           ide                                      Launch mirgae Web UI. (Now under development.)
    server             s                                        Launch debugging server.
    file               f                                        Create a new Python source file with copyrights doc string.

    help               h                                        Show usage of Mirage.
    version            v                                        Print version information.
    check              ?            update                      Check update
```

>> Detail documentation is now under construction.

More usage is [here](https://github.com/shotastage/django-mirage/tree/master/docs).

# 🤪  Author

- Shota Shimazu

# ©  License

Copyright © 2017-2018 Shota Shimazu All Rights Reserved.  
This software is released under the Apache License, see LICENSE for detail.
