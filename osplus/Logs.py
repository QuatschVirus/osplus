import time


class Normal(object):
    def __init__(self, path: str, print_out=False):
        self.path = path
        self.print = print_out
        if self.path[-4:] != '.log':
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
            with open(self.path, 'x')as f:
                f.write(f'{string}\n')

        if self.print:
            print(string)

    def reset(self):
        secs = time.time()
        stamp = f'{time.localtime(secs).tm_mday}.{time.localtime(secs).tm_mon}.{time.localtime(secs).tm_year} - {time.localtime(secs).tm_hour}:{time.localtime(secs).tm_min}:{time.localtime(secs).tm_sec}'
        string = f'[{stamp}] - osplus.Log.LogReset: The Log file in {self.path} was reset'
        with open(self.path, 'w') as f:
            f.write(string + '\n')
        print(string)
