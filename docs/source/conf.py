import os
import sys
sys.path.insert(0, os.path.abspath('../..'))  # remonte de 2 niveaux

project = 'Gestion de ferme'
author = 'Benjamin, Soufiane, Youssef, Harry'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

html_theme = 'sphinx_rtd_theme'