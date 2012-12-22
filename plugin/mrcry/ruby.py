import subprocess


def execute(expr):
    if not expr.startswith("print"):
        expr = "print " + expr

    return subprocess.check_output(['ruby', '-e', expr])
