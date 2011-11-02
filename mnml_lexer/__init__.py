from pygments.lexer import ExtendedRegexLexer, bygroups
from pygments.token import *

def _indentation(lexer, match, ctx):
    indentation = match.group(0)
    yield match.start(), Text, indentation
    ctx.last_indentation = indentation
    ctx.pos = match.end()

    if hasattr(ctx, 'block_state') and ctx.block_state and \
            indentation.startswith(ctx.block_indentation) and \
            indentation != ctx.block_indentation:
        ctx.stack.append(ctx.block_state)
    else:
        ctx.block_state = None
        ctx.block_indentation = None
        ctx.stack.append('content')

def _starts_block(token, state):
    def callback(lexer, match, ctx):
        yield match.start(), token, match.group(0)

        if hasattr(ctx, 'last_indentation'):
            ctx.block_indentation = ctx.last_indentation
        else:
            ctx.block_indentation = ''

        ctx.block_state = state
        ctx.pos = match.end()

    return callback

class MnmlLexer(ExtendedRegexLexer):
    name = 'Mnml'
    aliases = ['mnml']
    filenames = ['*.mnml']

    tokens = {
        'root': [
            (r'[ \t]*\n', Text),
            (r'[ \t]*', _indentation),
        ],
        'content': [
            (r'[a-z0-9_][a-zA-Z0-9_]*', Name.Tag, 'tag'),
            (r'#[^\n]*', Comment),
        ],
        'tag': [
            (r'(\s+)([a-z0-9_][a-zA-Z0-9_]*)(=)', bygroups(Text, Name.Attribute, Punctuation), 'value'),
            (r'\s+->\s*\n', _starts_block(Operator, 'heredoc'), '#pop:2'),
            (r'[ \t]+[^\n]*\n', Literal.String, '#pop:2'),
        ],
        'value': [
            (r'"(?:\\"|[^\n"])*"', Literal.Number, '#pop'),
            (r'\S*', Literal.Number, '#pop'),
        ],
        'heredoc': [
            (r'[^\n]+', Literal.String),
            (r'\n', Text, 'root'),
        ],
    }
