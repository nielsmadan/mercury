call venom#Load()

py << END_PY
if vim.venom.include_guard("mercury"):
    import vim

    class mercury(object):
        @staticmethod
        def run_python_file():
            vim.command("w !python<CR>")

    # vim.setAuGroupCmds("mercury",
    #         [vim.AutoCmd("FileType", "python", lambda: vim.noremap("<c-z>", mercury.run_python_normal))])
END_PY

if exists('g:mercury') || &cp
    finish
endif

augroup mercury
    au! FileType python noremap <c-z> :w !python<CR>
augroup END

echom "MERCURY LOADED"
