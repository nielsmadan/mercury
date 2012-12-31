import vim


def to_message(output):
    print output


def to_vert_split(output):
    vim.win.vnew()
    vim.current.buffer[:] = output.split('\n')[:-1]


def to_hor_split(output):
    vim.win.new()
    vim.current.buffer[:] = output.split('\n')[:-1]
