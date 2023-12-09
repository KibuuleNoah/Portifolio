from flask import Blueprint, render_template, url_for

vict_bp = Blueprint(
    "vict",
    __name__,
    template_folder="templates",
    url_prefix="/vict",
)


@vict_bp.route("/")
def index():
    return render_template("index.html")
