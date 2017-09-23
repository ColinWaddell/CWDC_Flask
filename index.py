import markdown
from flask import Flask, Markup, render_template

app = Flask(__name__)

@app.route("/")
def index():
    content = """
Chapter
=======

Section
-------

* Item 1
* Item 2
"""
    content = Markup(markdown.markdown(content))
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, use_reloader=True, host='0.0.0.0')
