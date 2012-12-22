import venom
import vim

from mrcry import src, dst, execute

if vim.g.is_defined("mercury_leader_seq"):
    leader_seq = vim.g.mercury_leader_seq
else:
   leader_seq = "<leader>r"

# def append_hello_world():
#     print "APPENDING HELLO WORLD"
#     vim.current.buffer.append("Hello World")

venom.py_fn_to_vim_command("MercuryLM", execute.build(src.line, dst.to_message))
venom.py_fn_to_vim_command("MercurySM", execute.build(src.selection, dst.to_message),
                           allow_range=True)

vim.map.nnoremap("%slm" % leader_seq, ":MercuryLM<CR>")
vim.map.vnoremap("%ssm" % leader_seq, ":MercurySM<CR>")

print "MERCURY LOADED"
