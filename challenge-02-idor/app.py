from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "nct_workshop_2026"

FLAG = "NCT{1d0r_1s_s0_34sy}"
ADMIN_ID = 7


def make_users():
    data = [
        {
            "id": 1,
            "name": "Minh Anh",
            "job": "Student",
            "bio": "Loves music and traveling.",
            "email": "minhanh01@gmail.com",
            "phone": "090 123 4501",
            "location": "Hanoi",
            "joined": "12/03/2022",
            "avatar": "🙂",
            "note": None,
            "is_admin": False,
        },
        {
            "id": 2,
            "name": "Hai Long",
            "job": "Software Engineer",
            "bio": "Passionate about programming and coffee.",
            "email": "hailong02@gmail.com",
            "phone": "090 123 4502",
            "location": "Ho Chi Minh City",
            "joined": "05/07/2021",
            "avatar": "🙂",
            "note": None,
            "is_admin": False,
        },
        {
            "id": 3,
            "name": "Thu Ha",
            "job": "Designer",
            "bio": "Enjoys reading books in the morning.",
            "email": "thuha03@gmail.com",
            "phone": "090 123 4503",
            "location": "Da Nang",
            "joined": "20/01/2023",
            "avatar": "🙂",
            "note": None,
            "is_admin": False,
        },
        {
            "id": 4,
            "name": "Quoc Bao",
            "job": "Marketing",
            "bio": "Often takes street photography.",
            "email": "quocbao04@gmail.com",
            "phone": "090 123 4504",
            "location": "Hai Phong",
            "joined": "08/09/2022",
            "avatar": "🙂",
            "note": None,
            "is_admin": False,
        },
        {
            "id": 5,
            "name": "Lan Anh",
            "job": "Accountant",
            "bio": "A huge football fan.",
            "email": "lananh05@gmail.com",
            "phone": "090 123 4505",
            "location": "Can Tho",
            "joined": "14/11/2020",
            "avatar": "🙂",
            "note": None,
            "is_admin": False,
        },
        {
            "id": 6,
            "name": "Duc Minh",
            "job": "Teacher",
            "bio": "Addicted to bubble tea and Korean dramas.",
            "email": "ducminh06@gmail.com",
            "phone": "090 123 4506",
            "location": "Hue",
            "joined": "30/04/2021",
            "avatar": "🙂",
            "note": None,
            "is_admin": False,
        },
        {
            "id": 7,
            "name": "Administrator",
            "job": "System Admin",
            "bio": "System administrator. Nothing to see here... or is there?",
            "email": "admin@nct-internal.com",
            "phone": "N/A",
            "location": "Internal",
            "joined": "01/01/2020",
            "avatar": "👤",
            "note": FLAG,
            "is_admin": True,
        },
        {
            "id": 8,
            "name": "Phuong Uyen",
            "job": "Sales",
            "bio": "Running every morning, gym every evening.",
            "email": "phuonguyen08@gmail.com",
            "phone": "090 123 4508",
            "location": "Nha Trang",
            "joined": "22/06/2022",
            "avatar": "🙂",
            "note": None,
            "is_admin": False,
        },
        {
            "id": 9,
            "name": "Tuan Kiet",
            "job": "Freelancer",
            "bio": "Loves games and anime.",
            "email": "tuankiet09@gmail.com",
            "phone": "090 123 4509",
            "location": "Binh Duong",
            "joined": "17/02/2023",
            "avatar": "🙂",
            "note": None,
            "is_admin": False,
        },
        {
            "id": 10,
            "name": "Ngoc Mai",
            "job": "Student",
            "bio": "Currently learning Japanese.",
            "email": "ngocmai10@gmail.com",
            "phone": "090 123 4510",
            "location": "Dong Nai",
            "joined": "03/10/2023",
            "avatar": "🙂",
            "note": None,
            "is_admin": False,
        },
        {
            "id": 11,
            "name": "Anh Tuan",
            "job": "Backend Developer",
            "bio": "Enjoys building APIs and tinkering with servers.",
            "email": "anhtuan11@gmail.com",
            "phone": "090 123 4511",
            "location": "Hanoi",
            "joined": "11/02/2022",
            "avatar": "🙂",
            "note": None,
            "is_admin": False,
        },
        {
            "id": 12,
            "name": "Bao Tran",
            "job": "QA Engineer",
            "bio": "Breaking software to make it better.",
            "email": "baotran12@gmail.com",
            "phone": "090 123 4512",
            "location": "Da Nang",
            "joined": "07/08/2021",
            "avatar": "🙂",
            "note": None,
            "is_admin": False,
        },
        {
            "id": 13,
            "name": "Khanh Nguyen",
            "job": "DevOps Engineer",
            "bio": "Automation enthusiast and Linux fan.",
            "email": "khanhnguyen13@gmail.com",
            "phone": "090 123 4513",
            "location": "Ho Chi Minh City",
            "joined": "19/05/2020",
            "avatar": "🙂",
            "note": None,
            "is_admin": False,
        },
        {
            "id": 14,
            "name": "Trang Le",
            "job": "UI/UX Designer",
            "bio": "Designing interfaces people love.",
            "email": "trangle14@gmail.com",
            "phone": "090 123 4514",
            "location": "Hue",
            "joined": "23/11/2022",
            "avatar": "🙂",
            "note": None,
            "is_admin": False,
        },
        {
            "id": 15,
            "name": "Thanh Pham",
            "job": "Data Analyst",
            "bio": "Enjoys turning data into stories.",
            "email": "thanhpham15@gmail.com",
            "phone": "090 123 4515",
            "location": "Can Tho",
            "joined": "02/04/2023",
            "avatar": "🙂",
            "note": None,
            "is_admin": False,
        },
    ]

    return {u["id"]: u for u in data}


USERS = make_users()

GIVEN_USER_ID = 3
GIVEN_USERNAME = "workshop_user"
GIVEN_PASSWORD = "nct2026"


@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("profile", id=session["user_id"]))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if username == GIVEN_USERNAME and password == GIVEN_PASSWORD:
            session["user_id"] = GIVEN_USER_ID
            return redirect(url_for("profile", id=GIVEN_USER_ID))
        else:
            error = "Invalid username or password."

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect(url_for("login"))

    try:
        target_id = int(request.args.get("id", session["user_id"]))
    except ValueError:
        return render_template("error.html", message="Invalid ID."), 400

    if target_id not in USERS:
        return render_template("error.html", message="User not found."), 404

    user = USERS[target_id]
    me = USERS[session["user_id"]]
    is_own = target_id == session["user_id"]

    return render_template("profile.html", user=user, me=me, is_own=is_own)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
