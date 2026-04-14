from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route("/")
def index():
    homepage = "<h1>蔡純珍Python網頁</h1>"
    homepage += '<a href="/today">顯示日期時間</a><br>'
    homepage += '<a href="/welcome?nick=純珍">傳送使用者暱稱</a><br>'
    homepage += '<a href="/account">網頁表單傳值</a><br>'
    homepage += '<a href="/math">數學四則運算</a><br>'
    homepage += '<a href="/me">個人簡介網頁</a><br>'
    return homepage

@app.route("/me")
def me():
    return render_template("me.html")

@app.route("/today")
def today():
    now = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
    return render_template("today.html", datetime=now)

@app.route("/welcome")
def welcome():
    user = request.args.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        return "您輸入的帳號是：" + user + "；密碼為：" + pwd
    return render_template("account.html")

@app.route("/math", methods=["GET", "POST"])
def math():
    result = None
    if request.method == "POST":
        try:
            x = float(request.form.get("x"))
            y = float(request.form.get("y"))
            opt = request.form.get("opt")
            if opt == "+": result = x + y
            elif opt == "-": result = x - y
            elif opt == "*": result = x * y
            elif opt == "/": result = x / y if y != 0 else "除數不能為0"
        except:
            result = "輸入錯誤"
    return render_template("math.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)