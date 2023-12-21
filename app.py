from flask import (
    Flask,
    render_template_string,
    send_file,
    request,
    render_template,
    url_for,
    abort,
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from API import GUI_PRO, NON_GUI, certs
from vann import love
import sqlite3, datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.register_blueprint(love)

db = SQLAlchemy(app)


class DataBase(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.String(5000))
    datetime = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())


@app.route("/", methods=["GET", "POST"])
def welcome():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        data = DataBase(name=name, email=email, message=message)
        db.session.add(data)
        db.session.commit()

    return render_template("welcome.html", certs=certs)


@app.route("/projects")
def projects():
    return render_template("base_projects.html", GUI=GUI_PRO, NON_GUI=NON_GUI)


@app.route("/viewmsg", methods=["POST", "GET"])
def media():
    if request.method == "POST":
        conn = sqlite3.connect("./instance/main.db")
        cursor = conn.cursor()
        pass_ = cursor.execute("SELECT adim FROM adim;").fetchone()[0]
        cursor.close()
        conn.close()
        if check_password_hash(pass_, request.form["password"]):
            clients = DataBase.query.all()
            return render_template("views.html", clients=clients)
        else:
            abort(403)
    return render_template_string(
        """
                                  <form method=POST>
                                    <input type="password" name="password" placeholder="Enter Your Password" required>
                                  </form>
                                  """
    )


# if __name__ == "__main__":
# app.run(debug=True)
app.app_context().push()
db.create_all()
