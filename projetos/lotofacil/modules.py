import sys
import os

path_script = os.path.dirname(__file__)
path_helpers = '../helpers'

sys.path.insert(0, os.path.join(path_script, path_helpers))

#importa os módulos extras
import helpers
