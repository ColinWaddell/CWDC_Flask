import markdown
from flask import Markup

def _load_md(filename):
    try:
        f = open('content/%s.md' % filename, 'r')
        raw_md = f.read()
    except FileNotFoundError:
        f = open('content/404.md', 'r')
        raw_md = f.read()
        raw_md = raw_md.replace('{{page_title}}', filename)
    
    md = Markup(markdown.markdown(raw_md))

    return md

def get_md(page):
    if isinstance(page, (tuple, list)):
        md = [_load_md(p) for p in page]
    else:
        md = _load_md(page)
    return md
