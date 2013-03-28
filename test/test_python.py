import unittest
from nose.tools import eq_
import string

import mercury


class TestPython(unittest.TestCase):
    def test_execute_simple(self):
        result = mercury.python.execute("print 'this'", "")

    def test_execute_auto_import_type_one(self):
        result = mercury.python.execute("print string.lowercase", ["import re\n", "import string\n"])

        eq_(string.lowercase + "\n", result)

        eq_(result, "this\n")

    def test_execute_simple_multiple(self):
        result = mercury.python.execute("print 'this'\nprint 'that'", "")

        eq_(result, "this\nthat\n")

    def test_execute_simple_indented(self):
        result = mercury.python.execute("    print 'this'", "")

        eq_(result, "this\n")

    def test_execute_complex_indented(self):
        result = mercury.python.execute(
                                    "     def foo(x):\n"
                                    "         return x * x\n"

                                    "     print foo(3)", "")

        eq_(result, "9\n")

    def test_execute_auto_import_type_one(self):
        result = mercury.python.execute("print string.lowercase", ["import re\n", "import string\n"])

        eq_(string.lowercase + "\n", result)

    def test_execute_auto_import_type_two(self):
        result = mercury.python.execute("print lowercase",
                                      ["import re\n", "from string import lowercase"])

        eq_(string.lowercase + "\n", result)

    def test_execute_add_print_expression_simple(self):
        result = mercury.python.execute("1 + 1", "")

        eq_(result, "2\n")

    def test_execute_add_print_expression_multi_line(self):
        result = mercury.python.execute("foo = 'what'\n1 + 1", "")

        eq_(result, "2\n")

    def test_execute_add_print_expression_multi_print(self):
        result = mercury.python.execute("print 'this'\nfoo = 'what'\n1 + 1", "")

        eq_(result, "this\n2\n")

    def test_execute_add_print_last_statement(self):
        result = mercury.python.execute("print 'this'\nfoo = 'what'", "")

        eq_(result, "this\n")
