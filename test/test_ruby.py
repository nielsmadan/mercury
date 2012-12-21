import unittest
import flexmock

import vim_stub
import venom_stub

import venom
import vim

import plugin.mercury as mercury


class TestE2E(unittest.TestCase):
    def setUp(self):
        flexmock.flexmock(venom)
        flexmock.flexmock(vim.opt).should_receive('filetype').and_return('ruby')

    def test_rlm(self):
        flexmock.flexmock(mercury)

        venom.should_receive("get_current_line").with_args(read_only=True).and_return(
                "[1, 2, 3, 4].map {|x| x * 2}").once()

        mercury.should_call("from_line").and_return("[1, 2, 3, 4].map {|x| x * 2}").once()

        mercury.should_call("execute").with_args("execute_expr", "[1, 2, 3, 4].map {|x| x * 2}").and_return(
                "[2, 4, 6, 8]").once()

        mercury.should_call("to_message").with_args("[2, 4, 6, 8]").and_return(None).once()

        _rlm = mercury.build_executor(mercury.from_line, "execute_expr", mercury.to_message)

        _rlm()
