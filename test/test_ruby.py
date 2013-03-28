import unittest
from nose.tools import eq_

import mercury


class TestRuby(unittest.TestCase):
    def test_execute_simple(self):
        result = mercury.ruby.execute("puts 'this'", "")

        eq_(result, "this\n")

    def test_execute_simple_multiple(self):
        result = mercury.ruby.execute("puts 'this'\nputs 'that'", "")

        eq_(result, "this\nthat\n")
