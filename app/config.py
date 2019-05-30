import os
from importlib import import_module

# Select the config file to import based on the ENV variable of the server
env = os.getenv('ENV', 'dev')
config_name = 'cfg.' + env
module = import_module(config_name)
config = module.config
