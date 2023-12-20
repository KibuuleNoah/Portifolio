from flask import Blueprint, render_template, render_template_string, request, url_for

love = Blueprint(
    "vann",
    __name__,
    template_folder="templates",
    url_prefix="/vanessa",
)


@love.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        password = request.form.get("password")
        if password and password == "vane$$a":
            return render_template("index.html")
    return render_template_string(
        """ <form method='POST'>
                <label for='password'>Enter Password Dear:
                    <br>
                    <br>
                    <input type='password' id='password' name='password'>
                </label>
                <br>
                <br>
                <button type='submit'>Enter</button>
            </form>
            """
    )
