import venom
import vim

from mrcry import src, dst, execute

venom.py_fn_to_vim_command("MercuryLM", execute.build(src.line, dst.to_message))
venom.py_fn_to_vim_command("MercurySM", execute.build(src.selection, dst.to_message),
                           allow_range=True)

if vim.g.is_defined("mercury_no_defaults") and vim.g.mercury_no_defaults == "1":
    pass

else:
    if vim.g.is_defined("mercury_leader_seq"):
        leader_seq = vim.g.mercury_leader_seq
    else:
        leader_seq = "<leader>r"

    # def append_hello_world():
    #     print "APPENDING HELLO WORLD"
    #     vim.current.buffer.append("Hello World")

    vim.map.nnoremap("%slm" % leader_seq, ":MercuryLM<CR>")
    vim.map.vnoremap("%ssm" % leader_seq, ":MercurySM<CR>")

print "MERCURY LOADED"
