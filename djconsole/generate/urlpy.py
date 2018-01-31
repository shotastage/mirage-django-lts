# -*- coding: utf-8 -*-
"""
Copyright 2017-2018 Shota Shimazu.

This software is licensed under the MIT, see LICENSE for detail.
"""

import textwrap

def create_urlpy_script(app):
    return textwrap.dedent(
'''
from django.conf.urls import url
from {app}.views import """YOUR_VIEW_CLASS"""

urlpatterns = [
    url(r'^url_letter/', """YOUR_VIEW_CLASS""".as_view(), name='starts'),
]

''').format(app=app).strip()
