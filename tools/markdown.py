import markdown
from flask import Markup, render_template, render_template_string
import time

def _helpers():
    return {
        'year': time.strftime("%Y")
    }

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

def render_template_and_markdown(template_name, pages, context={}):
    context.update({ title:fetch_markdown(title) for title in pages })
    context.update(_helpers())
    context.update(context)
    pre_render = render_template(template_name, **context)
    return render_template_string(pre_render, **context)
