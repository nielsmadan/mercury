import vim
import venom

import mrcry


def execute(exe_fn_name, code):
    ft_mod = getattr(mrcry, vim.opt.filetype)
    exe_fun = getattr(ft_mod, exe_fn_name)
    return exe_fun(code)


def build_executor(src_fn, exe_fn_name, dst_fn):
    def __inner():
        return dst_fn(execute(exe_fn_name, src_fn()))

    return __inner


def from_line():
    return venom.get_current_line(read_only=True)


def to_message(output):
    print output


# def append_hello_world():
#     print "APPENDING HELLO WORLD"
#     vim.current.buffer.append("Hello World")

venom.nnoremap("<leader>rlm", build_executor(from_line, "execute_expr", to_message))
print "MERCURY LOADED"
