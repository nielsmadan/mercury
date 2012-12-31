import vim


def to_message(output):
    print output


def to_vert_split(output):
    vim.win.vnew()
    vim.current.buffer[:] = output.split('\n')[:-1]
