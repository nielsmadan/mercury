import unittest
import flexmock

import vim_stub
import venom_stub

import venom
import vim

import plugin.mercury as mercury
import mercury

from nose.tools import eq_


class TestE2E(unittest.TestCase):
    def setUp(self):
        flexmock.flexmock(venom)
        flexmock.flexmock(vim.opt).should_receive('filetype').and_return('python')

    def test_rlm_python(self):
        flexmock.flexmock(mercury)

        venom.should_receive("get_current_line").with_args(read_only=True).and_return(
                "[x for x in range(3)]").once()

        mercury.should_call("src.line").and_return("[x for x in range(3)]").once()

        mercury.should_call("execute.run").with_args("[x for x in range(3)]", '').and_return(
                "[0, 1, 2]\n").once()

        mercury.should_call("dst.to_message").with_args("[0, 1, 2]\n").and_return(None).once()

        _rlm = mercury.execute.build(mercury.src.line, mercury.dst.to_message)

        _rlm()
