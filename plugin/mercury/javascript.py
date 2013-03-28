import mercury.util


def execute(code, buff):
    return mercury.util.run_command(['node', '-e', code])
