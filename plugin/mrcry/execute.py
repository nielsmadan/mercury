import vim
import mrcry


def run(code, buff):
    ft_mod = getattr(mrcry, vim.opt.filetype)
    exe_fun = getattr(ft_mod, "execute")
    return exe_fun(code, buff)


def build(src_fn, dst_fn):
    def __inner():
        return dst_fn(run(src_fn(), vim.current.buffer))

    return __inner
