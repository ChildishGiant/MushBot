import settings


def run(call,response):
    settings.textCommands[call]=response
    return None