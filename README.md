![Mirage](./docs/assets/logo.png)

[![Updates](https://pyup.io/repos/github/shotastage/django-mirage/shield.svg)](https://pyup.io/repos/github/shotastage/django-mirage/)
[![Python 3](https://pyup.io/repos/github/shotastage/django-mirage/python-3-shield.svg)](https://pyup.io/repos/github/shotastage/django-mirage/)
[![PyPI version](https://badge.fury.io/py/django-mirage.svg)](https://badge.fury.io/py/django-mirage)
[![PyPI](https://img.shields.io/pypi/pyversions/django-mirage.svg)]()
[![Build Status](https://travis-ci.org/shotastage/django-mirage.svg?branch=master)](https://travis-ci.org/shotastage/django-mirage)
[![GitHub release](https://img.shields.io/github/release/shotastage/django-mirage.svg)](https://github.com/shotastage/django-mirage/releases)
[![PyPI](https://img.shields.io/pypi/format/django-mirage.svg)]()
[![PyPI](https://img.shields.io/pypi/l/django-mirage.svg)](https://opensource.org/licenses/Apache-2.0)


>> This is LTS version of [MIRAGE Framework (now under construction)](https://github.com/shotastage/mirageframework).
>> New feature will be added to new version of MIRAGE.

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
```

>> Detail documentation is now under construction.

More usage is [here](https://github.com/shotastage/django-mirage/tree/master/docs).

# 🤪  Author

- Shota Shimazu

# ©  License

Copyright © 2017-2018 Shota Shimazu All Rights Reserved.  
This software is released under the Apache License, see LICENSE for detail.


[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fshotastage%2Fdjango-mirage.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fshotastage%2Fdjango-mirage?ref=badge_large)
