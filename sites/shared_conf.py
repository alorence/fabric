from os.path import join
from datetime import datetime

import alabaster

try:
    # Use ReadTheDocs default theme only if it is installed.
    # Simply installit via ``pip install sphinx_rtd_theme``
    import sphinx_rtd_theme  # noqa: F401
    html_theme = "sphinx_rtd_theme"
    extensions = []
except ImportError:
    # Alabaster theme + mini-extension
    html_theme_path = [alabaster.get_path()]
    extensions = ['alabaster']
    html_theme = 'alabaster'


# Paths relative to invoking conf.py - not this shared file
html_static_path = [join('..', '_shared_static')]
html_theme_options = {
}
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'searchbox.html',
        'donate.html',
    ]
}

# Regular settings
project = 'Fabric'
year = datetime.now().year
copyright = '%d Jeff Forcier' % year
master_doc = 'index'
templates_path = ['_templates']
exclude_trees = ['_build']
source_suffix = '.rst'
default_role = 'obj'
