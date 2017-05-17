__author__ = 'tom caruso'

from halp import halp


@halp
def this_will_fail():
    print(int('some string'))


if __name__ == '__main__':
    this_will_fail()
