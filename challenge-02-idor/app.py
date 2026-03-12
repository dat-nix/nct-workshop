from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "nct_workshop_2026"

FLAG = "NCT{1d0r_1s_s0_34sy}"
ADMIN_ID = 7

def make_users():
    data = [
        {
            "id": 1, "name": "Minh Anh", "job": "Sinh viên",
            "bio": "Yêu thích âm nhạc và du lịch.",
            "email": "minhanh01@gmail.com", "phone": "090 123 4501",
            "location": "Hà Nội", "joined": "12/03/2022",
            "avatar": "🙂", "note": None, "is_admin": False,
        },
        {
            "id": 2, "name": "Hải Long", "job": "Kỹ sư phần mềm",
            "bio": "Đam mê lập trình và cà phê.",
            "email": "hailong02@gmail.com", "phone": "090 123 4502",
            "location": "TP. Hồ Chí Minh", "joined": "05/07/2021",
            "avatar": "🙂", "note": None, "is_admin": False,
        },
        {
            "id": 3, "name": "Thu Hà", "job": "Designer",
            "bio": "Thích đọc sách vào buổi sáng.",
            "email": "thuha03@gmail.com", "phone": "090 123 4503",
            "location": "Đà Nẵng", "joined": "20/01/2023",
            "avatar": "🙂", "note": None, "is_admin": False,
        },
        {
            "id": 4, "name": "Quốc Bảo", "job": "Marketing",
            "bio": "Hay chụp ảnh đường phố.",
            "email": "quocbao04@gmail.com", "phone": "090 123 4504",
            "location": "Hải Phòng", "joined": "08/09/2022",
            "avatar": "🙂", "note": None, "is_admin": False,
        },
        {
            "id": 5, "name": "Lan Anh", "job": "Kế toán",
            "bio": "Fan cuồng bóng đá.",
            "email": "lananh05@gmail.com", "phone": "090 123 4505",
            "location": "Cần Thơ", "joined": "14/11/2020",
            "avatar": "🙂", "note": None, "is_admin": False,
        },
        {
            "id": 6, "name": "Đức Minh", "job": "Giáo viên",
            "bio": "Nghiện trà sữa và phim Hàn.",
            "email": "ducminh06@gmail.com", "phone": "090 123 4506",
            "location": "Huế", "joined": "30/04/2021",
            "avatar": "🙂", "note": None, "is_admin": False,
        },
        {
            "id": 7, "name": "Administrator", "job": "System Admin",
            "bio": "Quản trị hệ thống. Không có gì để xem ở đây... hoặc là có?",
            "email": "admin@nct-internal.com", "phone": "N/A",
            "location": "Internal", "joined": "01/01/2020",
            "avatar": "👤", "note": FLAG, "is_admin": True,
        },
        {
            "id": 8, "name": "Phương Uyên", "job": "Kinh doanh",
            "bio": "Chạy bộ mỗi sáng, gym mỗi chiều.",
            "email": "phuonguyen08@gmail.com", "phone": "090 123 4508",
            "location": "Nha Trang", "joined": "22/06/2022",
            "avatar": "🙂", "note": None, "is_admin": False,
        },
        {
            "id": 9, "name": "Tuấn Kiệt", "job": "Freelancer",
            "bio": "Mê game và anime.",
            "email": "tuankiet09@gmail.com", "phone": "090 123 4509",
            "location": "Bình Dương", "joined": "17/02/2023",
            "avatar": "🙂", "note": None, "is_admin": False,
        },
        {
            "id": 10, "name": "Ngọc Mai", "job": "Sinh viên",
            "bio": "Đang học tiếng Nhật.",
            "email": "ngocmai10@gmail.com", "phone": "090 123 4510",
            "location": "Đồng Nai", "joined": "03/10/2023",
            "avatar": "🙂", "note": None, "is_admin": False,
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
            error = "Sai tên đăng nhập hoặc mật khẩu."
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
        return render_template("error.html", message="ID không hợp lệ."), 400

    if target_id < 1 or target_id > 10:
        return render_template("error.html", message="User không tồn tại."), 404

    user = USERS[target_id]
    me = USERS[session["user_id"]]
    is_own = (target_id == session["user_id"])
    return render_template("profile.html", user=user, me=me, is_own=is_own)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
