from flask import Flask, session, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    LoginManager,
    login_user,
    login_required,
    current_user,
)
from flask_session import Session


app = Flask(__name__)
app.config["SECRET_KEY"] = "uduhfufew83248374279"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class PetMon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    rank = db.Column(db.String(50), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(100), nullable=False)
