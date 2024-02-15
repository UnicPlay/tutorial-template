# Configuration file for the Sphinx documentation builder.

# -- Project information
import sunpy_sphinx_theme

project = 'ooga booga'
copyright = 'fff'
author = 'zzz'

release = '0'
version = '00'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = "sunpy"

# -- Options for EPUB output
epub_show_urls = 'footnote'
