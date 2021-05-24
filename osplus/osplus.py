import random, json, time
from tkinter import *


def choose_random(*objects):
    if type(objects) is tuple:
        objects = list(objects)
    random.shuffle(objects)
    choose = random.randint(0, len(objects) - 1)
    selection = objects[choose]
    return selection


def random_sequence(length: int):
    sequence = ''
    for i in range(length + 1):
        sequence.join(chr(random.randint(97, 122)))


class FileTypeError(Exception):
    def __init__(self, file: str, path: str):
        self.file = file
        self.path = path
        super().__init__(self.file)
        super().__init__(self.path)

    def __str__(self):
        return f'Path {self.path} don\'t results in desired file type {self.file}'


class Notification:
    def __init__(self, title: str, msg: str, accept, cancel, help=None):
        """Defines a Notification using tkinter. accept, cancel and help (optional) need a function to be called on these events"""
        self.title = title
        self.msg = msg,
        self.accept = accept
        self.cancel = cancel
        self.help = help
        self.window = None

    def show(self):
        """Shows the defined Notification and triggers the specified events"""
        self.window = Tk()
        self.window.title(self.title)
        self.window.wm_attributes("-topmost", 1)
        Label(self.window, text=self.msg).pack()
        Button(self.window, text='OK', command=self.accpeted)
        Button(self.window, text='Abbrechen', command=self.cancelled)
        if self.help is not None:
            Button(self.window, text='Hilfe', command=self.helped)

    def accpeted(self):
        self.window.destroy()
        self.accept()

    def cancelled(self):
        self.window.destroy()
        self.cancel()

    def helped(self):
        self.help()

    def dismiss(self):
        """Dismisses the Notification manually"""
        self.window.destroy()


class Config:
    """A type for configuration files. Uses json"""
    def __init__(self, path: str):
        self.path = path
        if self.path[-5:] == '.json':
            try:
                with open(self.path, 'r') as f:
                    self.value = json.load(f)
            except FileNotFoundError:
                with open(self.path, 'x') as f:
                    json.dump(dict(), f, indent=4)
        else:
            print(f'Path "{self.path}" doesn\'t result in desired json')
            raise Exception(f'Path "{self.path}" doesn\'t result in desired log')

    def __str__(self):
        return '<osplus.Config object>'

    def get(self, objective: str):
        """Get the contents of a main branch"""
        with open(self.path, 'r') as f:
            return json.load(f)[objective]

    def set(self, objective: str, value):
        """Set the contents of a main branch"""
        self.value[objective] = value
        with open(self.path, 'w') as f:
            json.dump(self.value, f, indent=4)

    def reset(self):
        self.value = dict()
        with open(self.path, 'w') as f:
            json.dump(self.value, f, indent=4)

    def delete(self, objective: str):
        del self.value[objective]
        with open(self.path, 'w') as f:
            json.dump(self.value, f, indent=4)


class Log:
    def __init__(self, path: str, print_out=False):
        self.path = path
        self.print = print_out
        if self.path[-4:] != '.log':
            print(f'Path "{self.path}" doesn\'t result in desired log')
            raise Exception(f'Path "{self.path}" doesn\'t result in desired log')

    def log(self, logger: str, action: str, text: str):
        secs = time.time()
        stamp = f'{time.localtime(secs).tm_mday}.{time.localtime(secs).tm_mon}.{time.localtime(secs).tm_year} - {time.localtime(secs).tm_hour}:{time.localtime(secs).tm_min}:{time.localtime(secs).tm_sec}'
        string = f'[{stamp}] - {logger}.{action}: {text}'
        try:
            with open(self.path, 'a')as f:
                f.write(f'{string}\n')
        except FileNotFoundError:
            secs = time.time()
            stamp = f'{time.localtime(secs).tm_mday}.{time.localtime(secs).tm_mon}.{time.localtime(secs).tm_year} - {time.localtime(secs).tm_hour}:{time.localtime(secs).tm_min}:{time.localtime(secs).tm_sec}'
            string = f'[{stamp}] - osplus.Log.LogCreation: The log file in {self.path} was created since it was not found'

        if self.print:
            print(string)

    def reset(self):
        secs = time.time()
        stamp = f'{time.localtime(secs).tm_mday}.{time.localtime(secs).tm_mon}.{time.localtime(secs).tm_year} - {time.localtime(secs).tm_hour}:{time.localtime(secs).tm_min}:{time.localtime(secs).tm_sec}'
        string = f'[{stamp}] - osplus.Log.LogReset: The Log file in {self.path} was reset'
        with open(self.path, 'w') as f:
            f.write(string + '\n')
        print(string)
