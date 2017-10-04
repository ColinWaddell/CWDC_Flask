from flask import Flask, render_template, render_template_string, request
from flask_bootstrap import Bootstrap
from tools.markdown import fetch_markdown, render_template_and_markdown
from tools.publishing_details import get_page_details
from tools.moment import moment
from key import SECRET_KEY
from tools.contact import ContactForm, SendMessage
import sys
import json

SITE_TITLE = 'ColinWaddell.com'

app = Flask(__name__)
app.jinja_env.globals['moment'] = moment
Bootstrap(app)
app.secret_key = SECRET_KEY

@app.route("/")
def index():
    context = {
        'title': '%s :: Home' % SITE_TITLE,
        'form': ContactForm()
    }
    return render_template_and_markdown('index.html',
        ('blurb', 'projects', 'websites', 'contact', 'footer'), 
        context)

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        form = ContactForm()
        message = form.message.data
        if form.validate_on_submit() and len(message) < 1000:
            SendMessage(message)
            return grab_page('success')
        else:
            return grab_page('error')
    else:
        return grab_page('contact', {'form': ContactForm()})

@app.route('/<path:path>')
def grab_page(path, ctx=None):
    context = {
        'title': '%s :: %s' % (SITE_TITLE, path),
        'content': fetch_markdown(path),
        'page_details': get_page_details(path)
    }
    if ctx:
        context.update(ctx)
    
    return render_template_and_markdown('page.html',
        ('blurb', 'footer'), context)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.run(debug=False, use_reloader=True, host='0.0.0.0')
