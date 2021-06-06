import json, yaml


class JSON(object):
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
            raise Exception(f'Path "{self.path}" doesn\'t result in desired json file')

    def __str__(self):
        return '<osplus.Configs.JSON object>'

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


class YAML(object):
    """A type for configuration files. Uses yaml"""

    def __init__(self, path: str):
        self.path = path
        if self.path[-4:] == '.yml':
            try:
                with open(self.path, 'r') as f:
                    self.value = yaml.load(f)
            except FileNotFoundError:
                with open(self.path, 'x') as f:
                    yaml.dump(dict(), f, indent=4)
        else:
            raise Exception(f'Path "{self.path}" doesn\'t result in desired yml file')

    def __str__(self):
        return '<osplus.Configs.YAML object>'

    def get(self, objective: str):
        """Get the contents of a main branch"""
        with open(self.path, 'r') as f:
            return yaml.load(f)[objective]

    def set(self, objective: str, value):
        """Set the contents of a main branch"""
        self.value[objective] = value
        with open(self.path, 'w') as f:
            yaml.dump(self.value, f, indent=4)

    def reset(self):
        """Resets the config to an empty dictionary"""
        self.value = dict()
        with open(self.path, 'w') as f:
            yaml.dump(self.value, f, indent=4)

    def delete(self, objective: str):
        """Deletes the specified component of the main branch"""
        del self.value[objective]
        with open(self.path, 'w') as f:
            yaml.dump(self.value, f, indent=4)
