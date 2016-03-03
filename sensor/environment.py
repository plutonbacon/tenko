# Standard library dependencies.
import copy
import os

# Third-party dependencies.
from inifile import IniFile

DEFAULT_CONFIG = {
    'CONTROLLER_URL': 'tenko.example.com',
}

def update_config_from_ini(config, inifile):
    def set_simple(target, source_path):
        rv = config.get(source_path)
        if rv is not None:
            config[target] = rv

    set_simple(target='CONTROLLER_URL',
               source_path='env.controller_url')


class Config(object):

    def __init__(self, filename=None):
        self.filename = filename
        self.values = copy.deepcopy(DEFAULT_CONFIG)

        if filename is not None and os.path.isfile(filename):
            inifile = IniFile(filename)
            update_config_from_ini(self.values, inifile)

    def __getitem__(self, name):
        return self.values[name]


class Environment(object):

    def __init__(self):
        return

    def load_config(self):
        """Loads the current config."""
        return Config()