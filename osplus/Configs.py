import json


class Normal(object):
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
        """Resets the config to an empty dictionary"""
        self.value = dict()
        with open(self.path, 'w') as f:
            json.dump(self.value, f, indent=4)

    def delete(self, objective: str):
        """Deletes the specified component of the main branch"""
        del self.value[objective]
        with open(self.path, 'w') as f:
            json.dump(self.value, f, indent=4)
