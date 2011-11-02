from setuptools import setup

setup(
    name="Mnml Pygments Lexer",
    version="1.0.0",
    description="Pygments Lexer for the Mnml language",
    author="Emil Loer",
    author_email="emil@koffietijd.net",
    url="http://getmnml.com",
    packages=["mnml_lexer"],
    license="BSD",
    entry_points="[pygments.lexers]\nmnmllexer = mnml_lexer:MnmlLexer"
)
