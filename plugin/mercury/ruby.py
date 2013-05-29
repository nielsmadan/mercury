import subprocess


def execute(expr, buff):
    if "\n" not in expr and not expr.startswith("print") and not expr.startswith("puts"):
        expr = "print " + expr
        return subprocess.check_output(['ruby', '-e', expr]) + "\n"
    else:
        return subprocess.check_output(['ruby', '-e', expr])
