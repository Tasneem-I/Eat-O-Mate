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
from sqlalchemy import func, and_, select

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


class MealLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    meal_type = db.Column(db.String(50), nullable=False)
    feeling = db.Column(db.String(50), nullable=False)
    overeating = db.Column(db.String(10), nullable=False)
    undereating = db.Column(db.String(10), nullable=False)
    urge_to_binge = db.Column(db.String(10), nullable=False)
    urge_to_restrict = db.Column(db.String(10), nullable=False)
    eat_with = db.Column(db.String(50), nullable=False)



@login_manager.user_loader
def user_load(user_id):
    return Users.query.get(int(user_id))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/home")
def homes():
    return render_template("home_loggedin.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Users.query.filter_by(email=request.form.get("email")).first()
        if user.password == request.form.get("password"):
            login_user(user)
            session["user_id"] = user.id
            session["user"]= user.points
            logins= True
            return render_template("home_loggedin.html", login=logins, points= user.points)
    return render_template("login.html")

@app.route("/shop")
@login_required
def shop():
    points = current_user.points
    mons = EatMon.query.all()
    return render_template("monshop.html", points=points, mons=mons)

@app.route('/meallog')
@login_required
def meal_log():

    normal_meal_criteria = and_(
        MealLog.overeating == "False",
        MealLog.undereating == "False",
        MealLog.urge_to_binge == "False",
        MealLog.urge_to_restrict == "False"
    )

    normal_meals_subquery = (
        db.session.query(
            MealLog.userid,
            func.count(MealLog.id).label('normal_meal_count')
        ).filter(
            normal_meal_criteria
        ).group_by(MealLog.userid).subquery()
    )

    combined_results = db.session.query(
        normal_meals_subquery.c.userid,
        normal_meals_subquery.c.normal_meal_count,
        MealLog.eat_with,
        func.count(MealLog.id).label('times_eaten_with')
    ).outerjoin(
        normal_meals_subquery,
        normal_meals_subquery.c.userid == MealLog.userid
    ).filter(
        normal_meal_criteria
    ).group_by(
        normal_meals_subquery.c.userid, MealLog.eat_with
    ).order_by(
        normal_meals_subquery.c.userid, func.count(MealLog.id).desc()
    ).all()

    results = {}
    for row in combined_results:
        userid, normal_meal_count, eat_with, times_eaten_with = row
        if userid not in results:
            results[userid] = {
                'normal_meal_count': normal_meal_count,
                'eat_with_most': {
                    'eat_with': eat_with, 
                    'times_eaten_with': times_eaten_with
                } if eat_with else None
            }

    return render_template('normal_meals.html', results=results)
















































if __name__ == "__main__":
    app.run(debug=True)
