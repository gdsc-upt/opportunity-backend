import os
from typing import AnyStr, Callable

import yaml


class Config(object):
    def __init__(self, config_file):
        if not os.path.exists(config_file):
            raise FileNotFoundError('Could not find "config.yml" file. Make sure to read the instructions from README.md')

        with open(config_file) as file:
            self.__config = yaml.safe_load(file)
            if not self.__config:
                raise Exception('Config file is empty!')

    def get(self, var_name: AnyStr, default=None, cast: Callable = str, raise_error: bool = False):
        value = self.__config.get(var_name, None)
        if value is not None:
            value = cast(value)
            if isinstance(value, str):
                value = value.strip()
            return value

        if default is not None:
            return cast(default)

        if raise_error:
            raise LookupError(f'Cannot find value for setting {var_name}!')
        return None
