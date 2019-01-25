"""This module exports the Healthier plugin class."""

from SublimeLinter.lint import NodeLinter
import re

class Healthier(NodeLinter):
    """Provides an interface to healthier."""

    syntax = ('javascript', 'html', 'javascriptnext', 'javascript 6to5', 'javascript (babel)')
    cmd = 'healthier --stdin --verbose'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0.0'
    regex = r'^\s.+:(?P<line>\d+):(?P<col>\d+):(?P<message>.+)'
    selectors = {
        'html': 'source.js.embedded.html'
    }

    html_pattern = re.compile(r'(^.*\n)\s+$', re.DOTALL)

    npm_name = 'healthier'
    defaults = {
        'disable_if_not_dependency': True
    }

    def run(self, cmd, code):
        """
        If HTML syntax and the last line is just whitespace then remove it.
        Its probably just space before closing.
        script tag
        """
        if code and self.syntax == 'html':
            match = self.html_pattern.match(code)
            if match:
                code = match.group(1)
        return super(Healthier, self).run(cmd, code)