# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from datetime import date
import requests

# -- Project information -----------------------------------------------------

project = 'Open Babel'
author = 'The Open Babel Team'
# The latest version from the GitHub API
try:
    response = requests.get("https://api.github.com/repos/openbabel/openbabel/releases/latest")
    release = response.json()['tag_name']
except requests.exceptions.ConnectionError:
    release = "3.1.1"
version = release

year = date.today().year
copyright = f'©{year} {author}'



# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinxext.rediraffe',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_design',
    'sphinx_copybutton',
    'breathe',
    'myst_parser',
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# set up redirects
rediraffe_branch = 'main'
rediraffe_redirects = "redirects.txt"

# Make sure icons show in LaTeX / PDF output
sd_fontawesome_latex = True

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = 'docs'    # one file 
language = "en"             # default language

myst_substitutions = {
  "release": release,
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

#intersphinx_mapping = {
#    'python' : ('https://docs.python.org/3/', None),
#    'numpy'  : ('https://numpy.org/doc/stable/', None)
#}

# -- Options for Breathe --------

breathe_projects = { 'Open Babel': 'build/openbabel/docs/xml' }
breathe_default_project = 'Open Babel'
breathe_default_members = ('members', 'undoc-members', 'protected-members')

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme ='pydata_sphinx_theme'
html_show_sourcelink = False

html_baseurl = 'https://openbabel.github.io'

html_theme_options = {
    'github_url': 'https://github.com/openbabel/openbabel',
    'use_edit_page_button': True,
    'show_toc_level': 2,
    "header_links_before_dropdown": 6,
    'collapse_navigation': True,
    "logo": {
        "text": "Open Babel",
    },
    "icon_links": [
        {
            "name": "Twitter",
            "url": "https://twitter.com/OpenBabel",
            "icon": "fa-brands fa-square-x-twitter",
        },
    ],
}

html_context = {
    # 'github_url': 'https://github.com', # or your GitHub Enterprise interprise
    'github_user': 'openbabel',
    'github_repo': 'openbabel.github.io',
    'github_version': 'main',
    'doc_path': 'source/',
}

html_sidebars = {
    # omit the sidebar on the mainpage
  #'index': []
}

html_logo = '_static/openbabel.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ['_static', '_images']

html_css_files = [
    'custom.css',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


