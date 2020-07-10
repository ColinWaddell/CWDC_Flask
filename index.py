""" My markdown powered homepage """

from flask import Flask, request
from flask_bootstrap import Bootstrap
from tools.markdown import fetch_markdown, render_template_and_markdown
from tools.publishing_details import get_page_details
from tools.moment import Moment
from settings import Settings

# Setup Flask
app = Flask(__name__)
app.jinja_env.globals["moment"] = Moment
Bootstrap(app)


@app.route("/")
def index():
    """ Handle hompage requests """
    context = {
        "title": "%s %s Home" % (Settings.title, Settings.spacer),
    }
    return render_template_and_markdown(
        "index.html", ("blurb", "projects", "websites", "footer"), context
    )


@app.route("/<path:path>")
def grab_page(path, extra_context=None):
    """ General purpose handler for individual page requests """
    context = dict(
        {
            "title": "%s %s %s" % (Settings.title, Settings.spacer, path),
            "content": fetch_markdown(path),
            "page_details": get_page_details(path),
        },
        **extra_context if extra_context else {}
    )

    return render_template_and_markdown("page.html", ("blurb", "footer"), context)


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["BOOTSTRAP_SERVE_LOCAL"] = True
    app.run(debug=False, use_reloader=True, host="0.0.0.0")
