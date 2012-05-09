#!/usr/bin/env python
import sys

import logging
logging.disable(logging.CRITICAL)

from argparse import ArgumentParser 
from coverage import coverage

import tests.config
from django.test.simple import DjangoTestSuiteRunner


def run_tests(verbosity, *test_args):
    if not test_args:
        test_args = ['url_tracker']
    test_runner = DjangoTestSuiteRunner(verbosity=verbosity)
    num_failures = test_runner.run_tests(test_args)
    if num_failures:
        sys.exit(num_failures)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-c', '--coverage', dest='use_coverage', default=False,
                      action='store_true', help="Generate coverage report")
    parser.add_argument('-v', '--verbosity', dest='verbosity', default=1,
                      type=int, help="Verbosity of output")
    options, args = parser.parse_known_args()

    if options.use_coverage:
        print 'Running tests with coverage'
        c = coverage(source=['url_tracker'])
        c.start()
        run_tests(options.verbosity, *args)
        c.stop()
        print 'Generate HTML reports'
        c.html_report()
    else:
        print 'Running tests'
        run_tests(options.verbosity, *args)
