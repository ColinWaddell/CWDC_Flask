from flask import Flask, render_template, render_template_string
from flask_bootstrap import Bootstrap
from tools.markdown import fetch_markdown, render_template_and_markdown
from tools.publishing_details import get_page_details
from tools.moment import moment
import sys

SITE_TITLE = 'ColinWaddell.com'

app = Flask(__name__)
app.jinja_env.globals['moment'] = moment
Bootstrap(app)

@app.route("/")
def index():
    return render_template_and_markdown('index.html',
        ('blurb', 'projects', 'websites', 'contact', 'footer'), {'title': '%s :: Home' % SITE_TITLE})

@app.route('/<path:path>')
def catch_all(path):
    context = {
        'title': '%s :: %s' % (SITE_TITLE, path),
        'content': fetch_markdown(path),
        'page_details': get_page_details(path)
    }
    
    return render_template_and_markdown('page.html',
        ('blurb', 'footer'), context)

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.run(debug=True, use_reloader=True, host='0.0.0.0')
