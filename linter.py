"""This module exports the Standard plugin class."""

from SublimeLinter.lint import NodeLinter

import logging

class Healthier(NodeLinter):
    """Provides an interface to healthier."""

    cmd = 'healthier --stdin'
    name = 'Healthier'
    regex = (
        r'^\s+(?P<line>\d+):(?P<col>\d+)'
        r'\s+((?P<error>error)|(?P<warning>warning))'
        r'\s+(?P<message>.+)'
    )

    defaults = {
        'disable_if_not_dependency': True,
        'selector': 'source.js, source.jsx, source.ts, source.tsx',
        '--stdin-filename': '${file}',
    }
