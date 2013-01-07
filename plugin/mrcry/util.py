import subprocess
import threading


def run_command(cmd_list, timeout=5.0):
    process = [None]
    stdout = [None]
    stderr = [None]

    def proc_fn():
        process[0] = subprocess.Popen(cmd_list, universal_newlines=True, shell=False,
                                      stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout[0], stderr[0] = process[0].communicate()

    proc_thread = threading.Thread(target=proc_fn)
    proc_thread.start()
    proc_thread.join(timeout)

    if not proc_thread.is_alive():
        return stdout[0] + stderr[0]
    else:
        process[0].terminate()
        proc_thread.join(0.5)
        if proc_thread.is_alive():
            process[0].kill()

        return "--- MERCURY TIME OUT ---"
