from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from tools.markdown import fetch_markdown

SITE_TITLE = 'ColinWaddell.com'

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    title = '%s :: Home' % SITE_TITLE
    (blurb, projects, websites, contact, footer) = fetch_markdown(
        ('blurb', 'projects', 'websites', 'contact', 'footer'))
    return render_template('index.html', **locals())

@app.route('/<path:path>')
def catch_all(path):
    title = '%s :: %s' % (SITE_TITLE, path)
    (blurb, content) = fetch_markdown(('blurb', path))
    return render_template('page.html', **locals())

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.run(debug=True, use_reloader=True, host='0.0.0.0')
