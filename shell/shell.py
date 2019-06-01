import os


def execute_command(command_to_execute):
    command = os.popen(command_to_execute)
    result = command.read()
    command.close()
    return result


def execute_commands(commands_to_execute):
    command = os.popen(' && '.join(commands_to_execute))
    result = command.read()
    command.close()
    return result
