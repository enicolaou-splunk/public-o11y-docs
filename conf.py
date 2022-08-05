# -*- coding: utf-8 -*-
#
# Splunk Observability Cloud documentation build configuration file,
# created by sphinx-quickstart on Mon Apr 11 14:35:43 2016.
#
# Modified by jmalin 2021-03-24
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

tags.add('show_muted')
tags.add('show_all')
tags.remove('show_muted') 

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.join(os.path.abspath('.'), '_ext'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'tagging',
    'toggle',
    'newpage',
    'myst_parser',
    'sphinx_markdown_tables'
]



# Set myst_parser to automatically generate labels for h1, h2, and h3
# headings
# myst_heading_anchors = 3
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
# source_suffix = '.rst'
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
# Update the copyright date annually -- Barbara Snyder
project = u'Splunk'
copyright = u'2021 Splunk, Inc'
author = u'Splunk'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u''
# The full version, including alpha/beta/rc tags.
release = u''

# The language for content autogenerated by Sphinx.
#
# This is also used if you do content translation via gettext catalogs.
language = None

# There are two options for replacing |today|:
# 1. Set today to some non-false value, then it is used: today = ''
# 2. today_fmt is used as the format for a strftime call. today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store','z_cheat-sheets', 'README.md']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.

# html_theme_options = {
#
# }

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
html_title = u'Splunk Observability Cloud documentation'

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
# html_last_updated_fmt = None

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': [
#       'searchbox.html',
        'about.html',
        'fulltoc.html',
        'relations.html',
    ]
}

html_theme_options = {
    'logo_name': True,
    'github_button': False,
}

# Add permalinks; trying to determine how to change
# "Permalink to this headline" but so far, no success --barbara snyder
# See also signalfx-includes.css and signalfx-alabaster.css
# (search for permalink or headerlink)

html_add_permalinks = u'  🔗'

# Barbara Snyder

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'Splunkdoc'

# Example configuration for intersphinx: refer to the Python standard library.
# commenting out -- Barbara Snyder
# intersphinx_mapping = {'https://docs.python.org/': None}

# An RST prolog to add basic roles to style with CSS.
# Specify spans in signalfx-includes.css
# not-ok is red, ok is green, strong is bold in another font, note is bold purple.
# Anything here also shows up at the top of every page
# title is built-in so there's probably a better way

# /* ROLES: Usage is :role:NO SPACE `text` */
# /* e.g. this is :not-ok:`red` */
# Font for roles is set in signalfx-includes.css. Search for span.strong to find how to define them.

rst_prolog = """
.. role:: not-ok
.. role:: ok
.. role:: note
.. role:: strong
.. role:: title
.. role:: monospace
.. role:: strike



.. |br| raw:: html

   <br />

.. |hr| raw:: html

   <hr />
          
"""

# Barbara Snyder An RST epilog to add variable names for feature text replacement, and non-breaking space.
# Week of 9/29/16, replace mtab with "Muting Rules tab"
# April 27, 2017 add |hyph| for non-breaking hyphen
# 

rst_epilog = """
.. |ms| replace:: Metrics Sidebar
.. |mtab| replace:: Muting Rules tab
.. |sn| replace:: ServiceNow
.. |sv| replace:: secondary visualization
.. |openmenu| replace:: Open the Detector 
   menu by clicking the bell icon at the top right corner of a chart, 
   or next to a heading in the :ref:`Infrastructure Navigator<infra>`. 

.. |nbsp| unicode:: 0xA0
      :trim:

.. |hyph| unicode:: 0x2011
      :trim:

"""



def on_page_context(app, pagename, templatename, context, doctree):
    """
    This injects the ``get_local_toc`` function into the document.

    The logic around the builder is because the JSON and other HTML builders,
    they will error because we've added a Python function into the context.
    So we have to make sure we're only putting this into HTML builders,
    and ones that don't serialize the context.
    """
    if getattr(app.builder, 'implementation', None) or app.builder.format != 'html':
        return
    context['get_local_toc'] = app.builder._get_local_toctree


def determine_local_toc(app, pagename, templatename, context, doctree):
    """
    This code determines the set of documents that get a local TOC in the sidebar.

    Any new books can be added to the ``books`` list here,
    and they will be given the proper local TOC sidebar.

    The actual implementation is in ``_templates/fulltoc.html``,
    where we show the proper toc depending on the ``show_local_toc`` variable here.
    """
#     books = ['monitor-alert', 'admin-guide', 'analytics-docs']
# If you add a book here, check to see if you need to remove maxdepth in the index.rst for the doc
# NEVER MIND: books function no longer used 10/2018
    books = []
    localtoc = False
    for book in books:
        if pagename.startswith(book):
            localtoc = True
            break
    context['show_local_toc'] = localtoc
    

def setup(app):
    app.add_css_file('custom.css')
    app.add_css_file('signalfx-alabaster.css')
    app.add_css_file('signalfx-includes.css')
    app.add_js_file('signalfx-includes.js')
    app.add_js_file('jsonpull-splunk.js')
    app.add_js_file('showdown.min.js')
    app.connect('html-page-context', on_page_context)
    app.connect('html-page-context', determine_local_toc)

# Removed from above
#   app.add_stylesheet('signalfx-fonts.css')

html_baseurl = "https://docs.splunk.com/Observability/"
