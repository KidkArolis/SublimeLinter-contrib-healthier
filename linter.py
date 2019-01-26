"""This module exports the Healthier plugin class."""

import re
from SublimeLinter.lint import NodeLinter

class Healthier(NodeLinter):
    """Provides an interface to healthier."""

    cmd = 'healthier --stdin --verbose'
    regex = r'^\s.+:(?P<line>\d+):(?P<col>\d+):(?P<message>.+)'
    defaults = {
        'selector': 'source.js - meta.attribute-with-value',
        'disable_if_not_dependency': True
    }

    def on_stderr(self, stderr):
        if ('healthier: Friendly linter' in stderr):
            return
        else:
            logger.error(stderr)

    def run(self, cmd, code):
        return super().run(cmd, code)
