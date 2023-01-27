"""Sphinx configuration file."""
import os
import sys

# add example module to the python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


extensions = ["sphinx_sqlalchemy"]

html_theme = "furo"
