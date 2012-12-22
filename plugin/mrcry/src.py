import venom


def line():
    return venom.get_current_line(read_only=True)


def selection():
    return '\n'.join(venom.get_visual_selection(read_only=True))


def from_buffer():
    return venom.get_selection(read_only=True)
