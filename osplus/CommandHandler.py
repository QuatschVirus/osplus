from colorama import Fore, init
import sys

init(convert=True)


class SimpleCommandProcessor(object):
    class ErrorArgs:
        def __init__(self, error_type: str, error_input: str, error_msg: str, fatal: bool):
            self.type = error_type
            self.user_input = error_input
            self.msg = error_msg
            self.fatal = fatal

    def __init__(self, prompt='§'):
        self.prompt = prompt
        self.commands = dict()
        self.error_handlers = dict()
        self.active = False

    def command(self, name: str):
        def decorator(func):
            self.commands[name] = func
            return func
        return decorator

    def error(self, error_type: str):
        def decorator(func):
            self.error_handlers[error_type] = func
            return func
        return decorator

    def run(self):
        self.active = True
        while self.active:
            command = input(self.prompt)
            command_parsed = command.split(' ')
            try:
                self.commands[command_parsed[0]](command_parsed)
            except KeyError:
                self.raise_error('CommandNotFound', self.prompt + command, 'This command was not found.', False)

    def stop(self):
        self.active = False

    def raise_error(self, error_type: str, error_input: str, error_msg: str, fatal: bool):
        error = self.ErrorArgs(error_type, error_input, error_msg, fatal)
        try:
            self.error_handlers[error_type](error)
        except KeyError:
            print(f'''{Fore.RED}---ERROR---
            An error occurred
            UserInput: "{error_input}"
            {error_type}: {error_msg}
            ---ERROR---{Fore.RESET}''')
            if fatal:
                self.stop()
                sys.exit('ERROR')
