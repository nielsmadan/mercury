import venom
import mercury.util as util


def execute(code, buff):
    file_path = venom.get_temp_file_path() + ".cpp"
    code_file = open(file_path, "w")

    code_file.write("\n".join([
        "#include <iostream>",
        "int main(int argc, char *argv[]) {",
        code,
        "return 0;",
        "}"]))

    code_file.close()

    bin_path = venom.get_temp_file_path()
    result = util.run_command(["g++", file_path, "-o", bin_path])

    if result == "":
        return util.run_command([bin_path])
    else:
        return result
