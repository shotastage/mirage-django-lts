# coding: utf-8

import unittest
from mirage.command import log
from mirage import mirage


class mirageTest(unittest.TestCase):

    def setUp(self):
        log("Setup")

    def test_first(self):
        log("test first")


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(mirageTest))
    return suite
