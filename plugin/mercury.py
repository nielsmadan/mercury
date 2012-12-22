import venom

from mrcry import src, dst, execute


# def append_hello_world():
#     print "APPENDING HELLO WORLD"
#     vim.current.buffer.append("Hello World")

venom.py_fn_to_vim_command("MercuryLM", execute.build(src.line, dst.to_message))
venom.py_fn_to_vim_command("MercurySM", execute.build(src.selection, dst.to_message))

venom.nnoremap("<leader>rlm", execute.build(src.line, dst.to_message))
venom.vnoremap("<leader>rsm", execute.build(src.selection, dst.to_message))

print "MERCURY LOADED"
