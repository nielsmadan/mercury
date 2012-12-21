import sys
import types

import flexmock

if 'vim' not in sys.modules:
    _vim_stub = types.ModuleType('Dummy Vim Module', "Dummy")
    sys.modules['vim'] = _vim_stub

    import vim
    vim.command = lambda *args, **kwargs: None
    vim.eval = lambda *args, **kwargs: None

    class _dummy(object):
        filetype = None

    vim.opt = _dummy
