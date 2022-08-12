from flask import Flask, render_template
import os

from user import userBp
from todo import toDoBp
from utils.db import db


from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)

with app.app_context():
    db.create_all()

app.secret_key = os.environ.get("SECRET_KEY")

app.register_blueprint(userBp)
app.register_blueprint(toDoBp)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)


