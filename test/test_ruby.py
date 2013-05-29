import unittest
from nose.tools import eq_

import mercury


class TestRuby(unittest.TestCase):
    def test_execute_simple(self):
        result = mercury.ruby.execute("puts 'Hello, World'", "")

        eq_(result, "Hello, World\n")

    def test_execute_assignment(self):
        result = mercury.ruby.execute("x = 5", "")

        eq_(result, "5\n")

    def test_execute_list(self):
        result = mercury.ruby.execute("[1, 2, 3]", "")

        eq_(result, "[1, 2, 3]\n")

    def test_execute_simple_multiple(self):
        result = mercury.ruby.execute("puts 'Hello, World'\nputs 'Goodbye, World'", "")

        eq_(result, "Hello, World\nGoodbye, World\n")
