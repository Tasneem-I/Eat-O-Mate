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


class EatMon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    rank = db.Column(db.String(50), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(100), nullable=False)


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(40), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    usertype = db.Column(db.String(70), nullable=False)
    height = db.Column(db.Float, nullale=False)
    weight = db.Column(db.Float, nullable=False)


class MealEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    meal_type = db.Column(db.String(50), nullable=False)
    feeling = db.Column(db.String(50), nullable=False)
    overeating = db.Column(db.String(10), nullable=False)
    undereating = db.Column(db.String(10), nullable=False)
    urge_to_binge = db.Column(db.String(10), nullable=False)
    urge_to_restrict = db.Column(db.String(10), nullable=False)
    eat_with = db.Column(db.String(50), nullable=False)
