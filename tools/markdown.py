import markdown
from flask import Markup

def _load_md(filename):
    try:
        f = open('content/%s.md' % filename, 'r')
        raw_md = f.read()
    except FileNotFoundError:
        f = open('content/404.md', 'r')
        raw_md = f.read().replace('{{page_title}}', filename)

    return Markup(markdown.markdown(raw_md))

def fetch_markdown(page):
    return [_load_md(p) for p in page] if isinstance(page, (tuple, list)) else _load_md(page)
