import os
from subprocess import Popen, PIPE


def execute_commands(commands_to_execute, wait=True):
    process = Popen(
        ' && '.join(commands_to_execute),
        shell=True,
        stdout=PIPE,
        stdin=PIPE,
        stderr=PIPE,
    )
    if wait:
        process_return = list(process.communicate())
    process.stdin.close()
    if wait:
        command_exit_code = process.wait()
        process_return[0] = process_return[0].decode('UTF-8')
        process_return[1] = process_return[1].decode('UTF-8')
        return (process_return[0] + process_return[1], command_exit_code)
