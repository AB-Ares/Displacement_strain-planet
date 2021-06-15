import datetime
import Displacement_strain_planet

# Project information
year = datetime.date.today().year
project = "Displacement_strain_planet"
author = "Adrien Broquet"
version = "0.2.1"


# General configuration
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosectionlabel",
]

# Autosummary pages will be generated by sphinx-autogen instead of sphinx-build
autosummary_generate = True

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = ".rst"

# Options for HTML output
html_theme = "sphinx_rtd_theme"
html_theme_options = {"display_version": True}
html_static_path = ["_static"]
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True
html_title = project
html_short_title = project
html_logo = "../misc/bender.jpeg"

html_context = {}
