import settings


def run(client, msg, args):
    call = args[0]
    response = args[1]
    settings.textCommands[call]=response
    return None