import sys
import os


# define o diretorio de helpers
path_helpers = 'helpers'

# pega o diretório atual do arquivo, sobe um diretório e acessa helpers
base_path = os.path.join(os.path.dirname(__file__), '..', path_helpers)
sys.path.insert(0, os.path.join(base_path))

import helpers

