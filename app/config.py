import os
from importlib import import_module

env = os.getenv('ENV', 'dev')
config_name = 'cfg.' + env
module = import_module(config_name)
config = module.config
