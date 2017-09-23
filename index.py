import markdown
from flask import Flask, Markup, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

def load_md(filename):
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
        md = [load_md(p) for p in page]
    else:
        md = load_md(page)
    return md

@app.route("/")
def index():
    (title, projects, websites, contact, footer) = get_md(
        ('title', 'projects', 'websites', 'contact', 'footer'))
    return render_template('index.html', **locals())

@app.route('/<path:path>')
def catch_all(path):
    content = get_md(path)
    return render_template('page.html', **locals())

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.run(debug=True, use_reloader=True, host='0.0.0.0')
