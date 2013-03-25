import mrcry.util


def execute(code, buff):
    return mrcry.util.run_command(['node', '-e', code])
