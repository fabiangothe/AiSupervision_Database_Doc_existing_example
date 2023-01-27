"""Sphinx configuration file."""
import os
import sys

# add example module to the python path
#sys.path.insert(0, os.path.dirname(__file__))


#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
#sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath('.')), 'example'))
sys.path.insert(0, os.path.abspath("../"))
#sys.path.insert(0, os.path.join(os.path.abspath("../"), 'example'))



extensions = ["sphinx_sqlalchemy"]

html_theme = "furo"
