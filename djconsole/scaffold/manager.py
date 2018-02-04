# -*- coding: utf-8 -*-
"""
Copyright 2017-2018 Shota Shimazu.

This software is licensed under the MIT, see LICENSE for detail.
"""

from flask import Flask, render_template


class ScaffoldManager():
    
    @staticmethod
    def make_view():
        return render_template("not_implemented.html")
