import os
from importlib import import_module

#basedir = os.path.abspath(os.path.dirname(__file__))
env = os.getenv('ENV', 'dev')
config_name = 'cfg.' + env
module = import_module(config_name)
config = module.config
