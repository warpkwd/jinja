# -*- coding: utf-8 -*-
from pallets_sphinx_themes import ProjectLink, get_version

# Project --------------------------------------------------------------

project = "Jinja"
copyright = "2007 Pallets Team"
author = "Pallets Team"
release, version = get_version("Jinja2")

# General --------------------------------------------------------------

master_doc = "index"

extensions = ["sphinx.ext.autodoc", "sphinx.ext.intersphinx", "pallets_sphinx_themes"]

intersphinx_mapping = {"python": ("https://docs.python.org/3/", None)}

# HTML -----------------------------------------------------------------

html_theme = "jinja"
html_context = {
    "project_links": [
        ProjectLink("Donate to Pallets", "https://www.palletsprojects.com/donate"),
        ProjectLink("Jinja Website", "https://www.palletsprojects.com/p/jinja/"),
        ProjectLink("PyPI releases", "https://pypi.org/project/Jinja2/"),
        ProjectLink("Source Code", "https://github.com/pallets/jinja/"),
        ProjectLink("Issue Tracker", "https://github.com/pallets/jinja/issues/"),
    ]
}
html_sidebars = {
    "index": ["project.html", "versions.html", "searchbox.html"],
    "**": ["localtoc.html", "relations.html", "versions.html", "searchbox.html"],
}
singlehtml_sidebars = {"index": ["project.html", "versions.html", "localtoc.html"]}
html_static_path = ["_static"]
html_favicon = "_static/logo-small.png"
html_logo = "_static/logo-small.png"
html_show_sourcelink = False

# LaTeX ----------------------------------------------------------------

latex_documents = [
    (master_doc, "Jinja.tex", "Jinja Documentation", "Pallets Team", "manual")
]
latex_use_modindex = False
latex_elements = {
    "papersize": "a4paper",
    "pointsize": "12pt",
    "fontpkg": r"\usepackage{mathpazo}",
    "preamble": r"\usepackage{jinjastyle}",
}
latex_use_parts = True
latex_additional_files = ["jinjastyle.sty", "logo.pdf"]
