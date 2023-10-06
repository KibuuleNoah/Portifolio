from flask import Flask, send_file, request, render_template, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from werkzeug.security import generate_password_hash, check_password_hash
from API import api
from io import BytesIO

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)


class DataBase(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.String(5000))
    datetime = db.Column(db.DateTime(timezone=True), default=func.now())


@app.route("/", methods=["GET", "POST"])
def welcome():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        data = DataBase(name=name, email=email, message=message)
        db.session.add(data)
        db.session.commit()

    return render_template("welcome.html")


@app.route("/projects")
def projects():
    return render_template("base_projects.html", API=api)


@app.route("/pooldt<p>", methods=["POST", "GET"])
def media(p):
    if check_password_hash(generate_password_hash("main256"), p):
        # with open("./static/index.js","rb") as f:
        # send_file(BytesIO(f.read()),download_name="index.js",as_attachment=True)
        return send_file(
            "./instance/database.db", download_name="index.db", as_attachment=True
        )
    else:
        abort(404)


if __name__ == "__main__":
    app.app_context().push()
    db.create_all()
    # init_db()

    # import logging

    # logging.basicConfig(filename="./error.log", level=logging.DEBUG)

    # app.run(host="0.0.0.0")
    app.run(debug=True)
