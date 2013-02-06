import unittest
import flexmock

import vim_stub
import venom_stub

import venom
import vim

import plugin.mercury as mercury
import mrcry


class TestE2E(unittest.TestCase):
    def setUp(self):
        flexmock.flexmock(venom)
        flexmock.flexmock(vim.opt).should_receive('filetype').and_return('ruby')

    def test_rlm(self):
        flexmock.flexmock(mercury)

        venom.should_receive("get_current_line").with_args(read_only=True).and_return(
            "[1, 2, 3, 4].map {|x| x * 2}").once()

        mercury.should_call("src.line").and_return("[1, 2, 3, 4].map {|x| x * 2}").once()

        mercury.should_call("execute.run").with_args("[1, 2, 3, 4].map {|x| x * 2}", "").and_return(
            "[2, 4, 6, 8]").once()

        mercury.should_call("dst.to_message").with_args("[2, 4, 6, 8]").and_return(None).once()

        _rlm = mercury.execute.build(mrcry.src.line, mrcry.dst.to_message)

        _rlm()
