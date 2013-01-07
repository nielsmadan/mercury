import parser
import mrcry.util


def execute(code):
    code_lines = code.split("\n")
    last_expr_start_line = _find_last_expr(code_lines)

    if last_expr_start_line is not None:
        last_expr = "\n".join(code_lines[last_expr_start_line:])
        if not last_expr.startswith("print"):
            last_expr = "print " + last_expr
            code_lines[last_expr_start_line:] = last_expr.split("\n")

    return mrcry.util.run_command(['python', '-c', '\n'.join(code_lines)])


def _find_last_expr(code_lines):
    for x in range(len(code_lines) - 1, -1, -1):
        code = '\n'.join(code_lines[x:])
        try:
            parser.suite(code)
            try:
                parser.expr(code)
            except:  # last statement is not an expression
                return None

            return x
        except:
            pass

    return None
