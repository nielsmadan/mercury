import parser
import mrcry.util
import re


def execute(code):
    code_lines = code.split("\n")
    last_expr_start_line = _find_last_expr(code_lines)

    if last_expr_start_line is not None:
        last_expr = "\n".join(code_lines[last_expr_start_line:])
        if not last_expr.startswith("print"):
            last_expr = "print " + last_expr
            code_lines[last_expr_start_line:] = last_expr.split("\n")

    code_lines = remove_indent(code_lines)

    return mrcry.util.run_command(['python', '-c', '\n'.join(code_lines)])


def remove_indent(code_lines):
    _indent_regex = r'^(\s*).*'
    res = re.match(_indent_regex, code_lines[0])
    if len(res.group(1)) > 0:
        code_lines = [line[len(res.group(1)):] for line in code_lines]

    return code_lines


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
