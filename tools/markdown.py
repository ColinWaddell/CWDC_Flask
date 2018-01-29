''' Deal with the markdown pages '''

import time
from markdown import markdown
from flask import Markup, render_template, render_template_string


def _helpers():
    return {
        'year': time.strftime("%Y")
    }


def _load_md(filename):
    filelist = [
        'content/%s.md' % filename,
        'content/%s/index.md' % filename,
        'content/404.md'
    ]

    for file_md in filelist:
        try:
            file = open(file_md, 'r')
            raw_md = file.read().replace('{{page_title}}', filename)
        except FileNotFoundError:
            continue
        else:
            break

    return Markup(markdown(raw_md))


def fetch_markdown(page):
    ''' Load either single, or list of pages '''
    return [_load_md(p) for p in page] \
        if isinstance(page, (tuple, list)) else _load_md(page)


def render_template_and_markdown(template_name, pages, context=None):
    ''' Render page content into a template '''
    context.update({title: fetch_markdown(title) for title in pages})
    context.update(_helpers())
    context.update(context if context else {})
    pre_render = render_template(template_name, **context)
    return render_template_string(pre_render, **context)
