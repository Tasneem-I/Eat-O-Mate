from flask import Flask, session, render_template, request, url_for, redirect, flash, send_from_directory, jsonify
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
import  random, joblib

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
    height = db.Column(db.Float, nullable=False)
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


db.init_app(app)
with app.app_context():
    db.create_all()

with app.app_context():
    db.create_all()
    # Add initial pet monsters if not already added
    if not EatMon.query.first():
        mons = [
            EatMon(name="Fuzzlet", rank="Common", points=160, image="fuzzlet.jpeg"),
            EatMon(name="Twinkle Tuft", rank="Common", points=180, image="twinklefuft.jpeg"),
            EatMon(name="Mystic Mole", rank="Common", points=150, image="mysticmole.jpg"),
            EatMon(name="Aurora Puff", rank="Rare", points=300, image="aurorapuff.jpg"),
            EatMon(name="Dew Drop", rank="Rare", points=450, image="dewdrop.jpeg"),
            EatMon(name="Pixie Paw", rank="Rare", points=250, image="pixiepaw.jpeg"),
            EatMon(name="Lumin Puff", rank="Epic", points=600, image="luminpuff.jpeg"),
            EatMon(name="Fae Fox", rank="Epic", points=500, image="faefox.jpeg"),
            EatMon(name="Moon Whisk", rank="Legendary", points=800, image="moonwhisk.jpeg"),
            EatMon(name="Nebula Elder",rank="Legendary",points=770,image="nebulaelder.jpg",),
            EatMon(name="Whimsy Bee", rank="Legendary", points=890, image="whimsybee.jpeg"),
            EatMon(name="Moon Ripple",rank="Extinct",points=1200,image="Moonripple.jpeg",),
            EatMon(name="Glimmer Lynx",rank="Extinct",points=2000,image="glimmerlynx.jpeg",),
            EatMon(name="Frost Whisker",rank="Extinct",points=1600,image="frostwhisker.jpeg",),# Add more pet monsters as needed
        ]
        db.session.add_all(mons)
        db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

short_model = joblib.load("short_screen_model/final_dt.joblib")
@app.route("/")
def home():
    return render_template("landingpage.html")

@app.route("/home")
def homes():
    return render_template("feature.html")

@app.route("/anorexia")
def ano():
    return render_template("anorexia.html")

@app.route("/bullimia")
def bul():
    return render_template("bullimia.html")

@app.route("/binge")
def bin():
    return render_template("binge.html")

@app.route("/avoidant")
def avo():
    return render_template("avoidant.html")

@app.route("/signup_start")
def start():
    return render_template("EntrySignup.html")

@app.route("/longscreen")
def long():
    return render_template("LongScreening.html")

@app.route("/shortscreen")
def short():
    return render_template("ShortScreening.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        usertype = request.args.get('result')
        name = request.form.get("name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        height = request.form.get("height")
        weight = request.form.get("weight")
        points = 100
        user = Users(name=name, email=email, username=username, password=password,height=height,weight=weight, usertype=usertype,
points=points)
        db.session.add(user)
        db.session.commit()
        points = user.points
        login_user(user)
        return redirect(url_for("homes"))
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Users.query.filter_by(email=request.form.get("email")).first()
        if user.password == request.form.get("password"):
            login_user(user)
            session["user_id"] = user.id
            session["user"]= user.points
            logins= True
            return render_template("feature.html", login=logins, points= user.points)
    return render_template("login.html")

@app.route("/shop")
@login_required
def shop():
    points = current_user.points
    mons = EatMon.query.all()
    return render_template("monshop.html", points=points, mons=mons)

@app.route("/buy_mon", methods=["POST"])
@login_required
def buy_mon():
    mon_id = request.form.get("mon_id")
    mon = EatMon.query.get(mon_id)
    if mon and current_user.points >= mon.points:
        current_user.points -= mon.points
        db.session.commit()
        flash("Congratulations, you bought a EatiMon!!")
        return redirect(url_for('shop'))
    else:
        # You can add logic to save the purchase if needed
        flash("Not enough points, collect more points by completing quests")
    return redirect(url_for('shop'))

@app.route('/meallog')
@login_required
def meal_log():
    pts = current_user.points
    normal_meals = MealLog.query.filter_by(user_id=current_user.id, overeating="No", undereating="No").all()
    normal_meal_count = len(normal_meals)
    eat_with_counts = {}
    for meal in normal_meals:
        eat_with_counts[meal.eat_with] = eat_with_counts.get(meal.eat_with, 0) + 1
    most_common_eat_with =eat_with_counts and max(eat_with_counts, key=eat_with_counts.get) or 0
    return render_template('meallog.html', mc=normal_meal_count, ac=most_common_eat_with, points=pts)


@app.route('/distract', methods=["GET", "POST"])
@login_required
def distract(): 
    userpoints = current_user.points
    return render_template('/distractions_start.html', points= userpoints)

@app.route('/distract_session')
def distract_session():
    global img
    ex = ['static/cobra.png', 'static/downwarddog.png', 'static/halfbend.png', 'static/mountain.png', 'static/plank.png', 'static/seatbend.png', 'static/staff.png', 'static/warrior1.png']
    img = random.choice(ex)
    current_user.points = current_user.points + 20
    db.session.commit()
    pts = current_user.points
    return render_template('/distractions.html', img = img, points=pts), 200, {'Cache-Control': 'no-cache, no-store, must-revalidate'}



@app.route("/add_meal_log", methods=["POST"])
@login_required
def add_meal_log():
    data = request.get_json()
    new_log = MealLog(
        user_id=current_user.id,
        meal_type=data["meal_type"],
        feeling=data["feeling"],
        overeating=data["overeating"],
        undereating=data["undereating"],
        urge_to_binge=data["urge_to_binge"],
        urge_to_restrict=data["urge_to_restrict"],
        eat_with=data["eat_with"]
    )
    current_user.points+=20
    db.session.add(new_log)
    db.session.commit()
    return jsonify({
        "meal_type": new_log.meal_type,
        "feeling": new_log.feeling,
        "overeating": new_log.overeating,
        "undereating": new_log.undereating,
        "urge_to_binge": new_log.urge_to_binge,
        "urge_to_restrict": new_log.urge_to_restrict,
        "eat_with": new_log.eat_with
    })

@app.route("/get_meal_logs", methods=["GET"])
@login_required
def get_meal_logs():
    logs = MealLog.query.filter_by(user_id=current_user.id).all()
    return jsonify([
        {
            "meal_type": log.meal_type,
            "feeling": log.feeling,
            "overeating": log.overeating,
            "undereating": log.undereating,
            "urge_to_binge": log.urge_to_binge,
            "urge_to_restrict": log.urge_to_restrict,
            "eat_with": log.eat_with
        } for log in logs
    ])



if __name__ == "__main__":
    app.run(debug=True)