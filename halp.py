__author__ = 'tom caruso'

import re

from traceback import print_exc


def strip_chars(some_string):
    return re.sub(r'[^a-zA-Z\d\s]', '', some_string).replace(' ', '+')


def get_suggestions(error):
    print("Looks like you're having some trouble with '{}'".format(error.args[0]))
    print("Try this:")
    print("https://www.google.com/#q=python+" + strip_chars(error.args[0]) + '\n')

    print_exc()


def halp(wrapped):
    def try_it():
        try:
            wrapped()
        except Exception as e:
            get_suggestions(e)
    return try_it
