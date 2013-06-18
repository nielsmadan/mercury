import vim
import mercury


filetype_map = {
    "qml": "javascript",
}


def run(code, buff):
    if vim.opt.filetype in filetype_map:
        ft_mod = getattr(mercury, filetype_map[vim.opt.filetype])
    else:
        ft_mod = getattr(mercury, vim.opt.filetype)

    exe_fun = getattr(ft_mod, "execute")

    return exe_fun(code, buff)


def build(src_fn, dst_fn):
    def __inner():
        return dst_fn(run(src_fn(), vim.current.buffer))

    return __inner
