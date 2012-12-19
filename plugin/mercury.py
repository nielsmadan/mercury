import re
import subprocess

import vim
import venom


def run_python_file():
    vim.command("w !python<CR>")


def get_start_white_space(line):
    pass
    # return re.match(


def remove_minimal_indent(lines):
    pass
    # minimal_indent = min([


def run_python_line_to_message():
    line = venom.get_current_line(read_only=True)
    if not line.startswith("print"):
        line = "print " + line

    print subprocess.check_output(['python', '-c', line])

# def append_hello_world():
#     print "APPENDING HELLO WORLD"
#     vim.current.buffer.append("Hello World")

venom.nnoremap("<leader>r", run_python_line_to_message)
print "MERCURY LOADED"
