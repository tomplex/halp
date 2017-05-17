# HALP!

Sometimes we all need a little help. Sometimes, we're also too lazy to copy an error message, pop over to google and type in the error. `halp` does the hard part for you, and lets you easily get some help when your code keeps failing.

## Usage

Use as a decorator:

    @halp
    def this_will_fail():
        print(int('some string'))

Result:

    Looks like you're having some trouble with 'invalid literal for int() with base 10: 'some string''
    Try this:
    https://www.google.com/#q=python+invalid+literal+for+int+with+base+10+some+string
      
    Traceback (most recent call last):
      File "/home/tom/dev/halp/halp.py", line 23, in try_it
        wrapped()
      File "example.py", line 8, in this_will_fail
        print(int('some string'))
    ValueError: invalid literal for int() with base 10: 'some string'

`halp` conveniently swallows that nasty error, while providing some helpful feedback, and the original erorr message.

Never manually search for a specific error again!

## Installation

Unfortunately, this isn't yet available on pypi. For now, you'll need to `git clone https://github.com/tomplex/halp` and then run `python setup.py install` with the desired python distribution. Compatible with python 3+.

## TODO

- return multiple links to specific answers
- use as a context manager
- who knows


## Contributing

Pull requests welcome!
