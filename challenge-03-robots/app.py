from flask import Flask, render_template, Response

app = Flask(__name__)

FLAG = "NCT{r0b0ts_4r3_n0t_s3cr3t}"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# robots.txt — đây là nơi người chơi cần tìm
@app.route("/robots.txt")
def robots():
    content = """User-agent: *
Disallow: /admin-panel
"""
    return Response(content, mimetype="text/plain")


# Trang ẩn chứa flag
@app.route("/admin-panel")
def admin_panel():
    return render_template("admin_panel.html", flag=FLAG)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
