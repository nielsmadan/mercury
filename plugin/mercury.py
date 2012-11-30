import vim
import venom


def run_python_file():
    vim.command("w !python<CR>")


def append_hello_world():
    print "APPENDING HELLO WORLD"
    # vim.current.buffer.append("Hello World")


venom.nnoremap("<leader><f7>", append_hello_world)
print "MERCURY HAS RUN"
