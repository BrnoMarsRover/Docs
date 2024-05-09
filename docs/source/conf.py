project = 'Brno Mars Rover Docs'
copyright = '2024, Adam Ligocki'
author = 'Adam Ligocki'

extensions = [
    'sphinx_rtd_theme',
    'myst_parser',
    'rst2pdf.pdfbuilder',
]
html_theme = "sphinx_rtd_theme"
pdf_documents = [('index', u'docs', u'Doc Name', u'Authors'),]

templates_path = ['_templates']
exclude_patterns = []
html_static_path = ['_static']
