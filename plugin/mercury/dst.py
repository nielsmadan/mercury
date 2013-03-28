import venom
import vim


def to_message(output):
    print output


def to_register(output):
    if "mercury_default_register" in vim.g:
        vim.registers.set(vim.g.mercury_default_register, output)
    else:
        destination_register = vim.fn.input("Destination register: ")
        vim.registers.set(destination_register, output)


def to_selection(output):
    venom.replace_visual_selection(output)


def to_vert_split(output):
    vim.win.vnew()
    vim.current.buffer[:] = output.split('\n')[:-1]
    vim.extbuffer(vim.current.buffer).buftype = "nofile"


def to_hor_split(output):
    vim.win.new()
    vim.current.buffer[:] = output.split('\n')[:-1]
    vim.extbuffer(vim.current.buffer).buftype = "nofile"
