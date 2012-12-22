import vim
import mrcry


def run(code):
    ft_mod = getattr(mrcry, vim.opt.filetype)
    exe_fun = getattr(ft_mod, "execute")
    return exe_fun(code)


def build(src_fn, dst_fn):
    def __inner():
        return dst_fn(run(src_fn()))

    return __inner
