#!/usr/bin/env python
"""
Lists/Executes the tests in the contrail test modules.

Usage:
    Lists the test features:
    ------------------------
    python tools/contrail-test.py list

    Lists the tests in set of features:
    -----------------------------------
    python tools/contrail-test.py list -f <feature1> <feature2> ....<featureN>
        Note: <feature1> <feature2> ....<featureN> are the feature
              listed by the above command

    Lists the tests with particular tag:
    ---------------------------------
    python tools/contrail-test.py list -t <tag> -d </path/to/contrail-test/>

    Run the list of tests:
    ----------------------
    python tools/contrail-test.py run -T <test1> <test2> ....<testN>
        Note: <test1> <test2> ....<testN> are the tests
              listed by the avove command.

    Documentation of the testcases:
    ------------------------------
    python tools/contrail-test.py doc -f <feature1> -t <tag> -d </path/to/contrail-test/>
"""

import os
import re
import sys
import argparse
from testtools.testsuite import iterate_tests
from fabric.api import lcd, local, settings
try:
   from unittest2 import TestLoader, TextTestRunner
except:
   from unittest import TestLoader, TextTestRunner

FEATURE_ROOTS = ('scripts', 'serial_scripts')

def parse_args():
    parser = argparse.ArgumentParser()
    defaults = {
    }
    parser.set_defaults(**defaults)
    parser.add_argument("operation", help="Operation to be performed [list | run | doc]")
    parser.add_argument("-d", "--test-dir", help="contrail-test root directory",
                        default=os.path.join(os.path.dirname(__file__), os.pardir))
    parser.add_argument("-f", "--features", nargs='+', help="List of test features")
    parser.add_argument("-T", "--tests", nargs='+', help="List of tests to execute")
    parser.add_argument("-t", "--tag", help="testcases matching specific tag")

    return parser.parse_args(sys.argv[1:])

class ContrailTest(object):
    def __init__(self, cmd_args):
        self.operation = cmd_args.operation
        self.testroot = cmd_args.test_dir
        self.features = cmd_args.features or []
        self.tag = cmd_args.tag
        self.tests = cmd_args.tests or []
        self.python_paths = [self.testroot,
                        '%s/fixtures/' % self.testroot,
                        '%s/scripts/' % self.testroot,
                        '%s/serial_scripts/' % self.testroot]
        for path in self.python_paths:
            sys.path.insert(0, os.path.realpath(path))
            os.environ["PYTHONPATH"] = os.environ.get("PYTHONPATH",'./')+':'+path
        if self.tag:
            os.environ["TAGS"] = self.tag
        self.testcases = self.get_all_tests()

        for feature in self.features:
            for featureroot in FEATURE_ROOTS:
                self.tests.append('.'.join([featureroot, feature]))
        if self.tests or self.tag:
            self.testcases = self.filter_testcases()

    def filter_testcases(self):
        testcases = list() if self.tests else self.testcases
        if self.tests:
            for testcase in self.testcases:
                for test in self.tests:
                    if re.match('%s[\.\[]'%test, testcase.id()) or \
                       test == testcase.id():
                        testcases.append(testcase)
                        break
        filtered_tc = list() if self.tag else testcases
        if self.tag:
           for testcase in testcases:
                fn = testcase._get_test_method()
                attributes = getattr(fn, '__testtools_attrs', None)
                if self.tag in (attributes or []):
                     filtered_tc.append(testcase)
        return filtered_tc

    def get_all_tests(self):
        tests = TestLoader().discover(self.testroot)
        return [test for test in iterate_tests(tests)]

    def do(self):
        """Do tests listing or execution"""
        if self.operation == 'list':
            self.list_tests()
        elif self.operation == 'run':
            self.run_tests()
        elif self.operation == 'doc':
            self.get_doc()

    def get_doc(self):
        ''' Get description of testcases '''
        for testcase in self.testcases:
            print testcase._testMethodName, '\n', testcase._testMethodDoc

    def list_tests(self):
        """Lists the test features and
           tests of a test feature or set of test modules."""
        for testcase in self.testcases:
            print testcase.id()

    def run_tests(self):
        """Executes the set of tests."""
        with lcd(self.testroot), settings(warn_only=True):
            for testcase in self.testcases:
                if '[' in testcase.id():
                    tc = re.match('(.*)\[', testcase.id()).group(1)
                else:
                    tc = testcase.id()
                local("python -m testtools.run %s" % (tc))

def main():
   ContrailTest(parse_args()).do()

if __name__ == '__main__':
    sys.exit(main())
