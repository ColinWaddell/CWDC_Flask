from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from tools.markdown import fetch_markdown

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    (title, projects, websites, contact, footer) = fetch_markdown(
        ('title', 'projects', 'websites', 'contact', 'footer'))
    return render_template('index.html', **locals())

@app.route('/<path:path>')
def catch_all(path):
    content = fetch_markdown(path)
    return render_template('page.html', **locals())

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.run(debug=True, use_reloader=True, host='0.0.0.0')
