import vim
import mercury


filetype_map = {
    "qml": "javascript",
}


def __get_filetype_module():
    filetype = (vim.opt.filetype if vim.opt.filetype not in filetype_map else
                filetype_map[vim.opt.filetype])

    available_filetypes = [key for key in dir(mercury) if not key.startswith("__") and
                           key not in ["dst", "execute", "src", "util"]]

    if filetype in available_filetypes:
        return getattr(mercury, filetype)
    elif ("mercury_default_filetype" in vim.g and
          vim.g.mercury_default_filetype in available_filetypes):
        return getattr(mercury, vim.g.mercury_default_filetype)


def run(code, buff):
    filetype_module = __get_filetype_module()

    if filetype_module is not None:
        execution_fn = getattr(filetype_module, "execute")

        return execution_fn(code, buff)
    else:
        print "mercury error: filetype not recognized and no default set",
        return ""


def build(src_fn, dst_fn):
    def __inner():
        return dst_fn(run(src_fn(), vim.current.buffer))

    return __inner
