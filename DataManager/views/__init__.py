import glob
from os import listdir
from os.path import dirname, basename, isfile, join
for i in listdir(join("DataManager", "views")):
    if i.endswith(".py") and not i == "__init__.py":
        i = i[:-3]
        exec(f'from .{i} import {i}')

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
