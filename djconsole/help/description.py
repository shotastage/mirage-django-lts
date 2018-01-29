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

usage = """
Django Console v0.0.12

Usage:
    djc [action] option <--sub-option> <inputs>

    djc [action]:[subaction] <--sub-option> <inputs>


Actions:
    newproject         new          Create a new Django project.
    newproject:cms     new:cms      Create a new Django CMS project. ( Django CMS is required. )
    console            c            Launch Django Python shell.
    console:db         c:db         Launch databse shell.
    database:migrate   db:migrate   Make migrations and apply migrations.
    database:reset     db:reset     Reset all database. ( Only debugging SQLite is supported. )

    help               h            Show usage of Django Console.
    version            v            Print version information.
"""

version = """
Django Console Version 0.0.12

Copyright (c) 2017-2018 Shota Shimazu
This software is licensed under the Apache v2, see LICENSE for detail.
"""
