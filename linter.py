"""This module exports the Healthier plugin class."""

import json
import logging
import re
from SublimeLinter.lint import NodeLinter

logger = logging.getLogger('SublimeLinter.plugin.healthier')

class Healthier(NodeLinter):
    """Provides an interface to the healthier executable."""

    cmd = 'healthier --format json --stdin'

    line_col_base = (1, 1)
    defaults = {
        'selector': 'source.js - meta.attribute-with-value'
    }

    def on_stderr(self, stderr):
        if (
            'DeprecationWarning' in stderr
            or 'ExperimentalWarning' in stderr
            or 'in the next version' in stderr  # is that a proper deprecation?
        ):
            logger.warning(stderr)
        else:
            logger.error(stderr)
            self.notify_failure()

    def find_errors(self, output):
        """Parse errors from linter's output."""
        try:
            # It is possible that users output debug messages to stdout, so we
            # only parse the last line, which is hopefully the actual healthier
            # output.
            # https://github.com/SublimeLinter/SublimeLinter-eslint/issues/251
            last_line = output.rstrip().split('\n')[-1]
            content = json.loads(last_line)
        except ValueError:
            logger.error(
                "JSON Decode error: We expected JSON from 'healthier', "
                "but instead got this:\n{}\n\n"
                "Be aware that we only parse the last line of above "
                "output.".format(output))
            self.notify_failure()
            return

        if logger.isEnabledFor(logging.INFO):
            import pprint
            logger.info(
                '{} output:\n{}'.format(self.name, pprint.pformat(content)))

        for entry in content:
            for match in entry['messages']:
                if match['message'].startswith('File ignored'):
                    continue

                column = match.get('column', None)
                ruleId = match.get('ruleId', '')
                if column is not None:
                    # apply line_col_base manually
                    column = column - 1

                yield (
                    match,
                    match['line'] - 1,  # apply line_col_base manually
                    column,
                    ruleId if match['severity'] == 2 else '',
                    ruleId if match['severity'] == 1 else '',
                    match['message'],
                    None  # near
                )

    def reposition_match(self, line, col, m, vv):
        match = m.match
        if (
            col is None
            or 'endLine' not in match
            or 'endColumn' not in match
        ):
            return super().reposition_match(line, col, m, vv)

        # apply line_col_base manually
        end_line = match['endLine'] - 1
        end_column = match['endColumn'] - 1

        for _line in range(line, end_line):
            text = vv.select_line(_line)
            end_column += len(text)

        return line, col, end_column
