# Mnml syntax lexer for Pygments

This package contains a Pygments Lexer for the [Mnml](http://github.com/thedjinn/mnml) language.o

## Installation

The lexer is available as a Pip package:

    pip insatll mnml-pygments-parser

Alternatively, to install from the git repository: (you may need to sudo depending on your Python environment)

    python setup.py install

## Usage

After installation the Mnml lexer automatically registers itself for files with the `.mnml` extension. Therefore, usage is easy:

    pygmentize document.mnml

You can also manally indicate you want to use the Mnml lexer by using a command line flag:

    pygmentize -l mnml somefile 

## Contribute

If you found a bug, don't hesitate to make a pull request.

## License

The Mnml lexer is licensed under the same terms as Pygments itself, which is the BSD license.
