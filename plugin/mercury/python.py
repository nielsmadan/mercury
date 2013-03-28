import parser
import mercury.util
import re


_STD_MODULES = ['re', 'random', 'itertools', 'string']
_IMPORT_1_REGEX = re.compile(r'^import (\S+)')
_IMPORT_2_REGEX = re.compile(r'^from (\S+) import (\S+)')

_INDENT_REGEX = re.compile(r'^(\s*).*')


def execute(code, buff):
    code_lines = code.split("\n")
    last_expr_start_line = _find_last_expr(code_lines)

    if last_expr_start_line is not None:
        last_expr = "\n".join(code_lines[last_expr_start_line:])
        if not last_expr.startswith("print"):
            last_expr = "print " + last_expr
            code_lines[last_expr_start_line:] = last_expr.split("\n")

    code_lines = _remove_indent(code_lines)

    import_lines = _find_std_imports(buff)

    return mercury.util.run_command(['python', '-c', '\n'.join(import_lines + code_lines)])


def _remove_indent(code_lines):
    res = re.match(_INDENT_REGEX, code_lines[0])
    if len(res.group(1)) > 0:
        code_lines = [line[len(res.group(1)):] for line in code_lines]

    return code_lines


def _find_std_imports(lines):
    res = []
    for line in lines:
        m = re.search(_IMPORT_1_REGEX, line)
        if m is not None and m.group(1) in _STD_MODULES:
            res.append(line)
        else:
            m = re.search(_IMPORT_2_REGEX, line)
            if m is not None and m.group(1) in _STD_MODULES:
                res.append(line)

    return res


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
