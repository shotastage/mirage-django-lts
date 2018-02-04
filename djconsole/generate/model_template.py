# -*- coding: utf-8 -*-
"""
Copyright 2017-2018 Shota Shimazu.

This software is licensed under the MIT, see LICENSE for detail.
"""

import textwrap

def create_model_py(class_name, contents):

    return "\n\n" + textwrap.dedent(
'''
class {class_name}(models.Model):
{contents}

''').format(class_name=class_name, contents=contents).strip() + "\n"
