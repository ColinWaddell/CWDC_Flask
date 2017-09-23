import markdown
from flask import Flask, Markup, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

def load_md(filename):
    f = open('content/%s.md' % filename, 'r')
    raw_md = f.read()
    md = Markup(markdown.markdown(raw_md))
    return md

def get_md(page):
    try:
        md = load_md(page)
    except FileNotFoundError:
        md = load_md('404')

    return md

@app.route("/")
def index():
    title = get_md('title')
    projects = get_md('projects')
    websites = get_md('websites')
    contact = get_md('contact')
    footer = get_md('footer')
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.run(debug=True, use_reloader=True, host='0.0.0.0')
