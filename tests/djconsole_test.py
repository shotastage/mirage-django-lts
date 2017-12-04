# coding: utf-8

import unittest
from djconsole.command import log
from djconsole import djconsole


class DjconsoleTest(unittest.TestCase):

    def setUp(self):
        log("Setup")

    def test_first(self):
        log("test first")


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(DjconsoleTest))
    return suite
