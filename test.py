__author__ = 'tom caruso'

import unittest
from halp import halp, get_suggestions, strip_chars


def this_should_fail():
    return {}['fail']


def this_shouldnt_fail():
    return str('plz halp')


class TestHalp(unittest.TestCase):

    def test_strip_chars(self):
        self.assertEqual(strip_chars("this is() a& test str1ng"), "this+is+a+test+str1ng")

    def test_halp(self):
        pass