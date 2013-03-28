import unittest
from nose.tools import eq_

import mercury


class TestE2E(unittest.TestCase):
    def test_execute_simple(self):
        result = mercury.javascript.execute("console.log('this');", "")

        eq_(result, "this\n")

    def test_execute_simple_multiple(self):
        result = mercury.javascript.execute("console.log('this');\nconsole.log('that')\n", "")

        eq_(result, "this\nthat\n")
