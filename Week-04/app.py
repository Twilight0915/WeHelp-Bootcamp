from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session

# 建立 Application 物件，設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)
# 設定session密鑰
app.secret_key = "Week-04 assignment"


# 建立路徑 / 對應的處理函式
@app.route("/")
def index():
    return render_template("index.html")


# 建立路徑 / signin
# 使用 POST方法
@app.route("/signin", methods=["POST"])
def signin():
    # 接收 POST 方法的 Query String
    id = request.form["id"]
    password = request.form["password"]
    # print(id)
    # print(password)
    if (id == "test" and password == "test"):
        # return "恭喜您，成功登入系統"
        # 導向路徑"/member"
        # session["欄位名稱"] = 存放的資料
        session["id"] = id
        # print(session)                      # {'id': 'test'}
        return redirect("/member")

    # 空字串表示: len(id) == 0   id=""
    elif (id == "" or password == ""):
        return redirect("/error?message=請輸入帳號、密碼")

    elif (id != "test" or password != "test"):
        return redirect("/error?message=帳號、或密碼輸入錯誤")


# 建立 /member路徑對應的處理函式
# 判斷session{}裡面是否有"id"，如果沒有,導回首頁
@app.route("/member")
def member():
    if "id" in session:                # 檢測session{} 裡面有沒有id這個 key
        return render_template("member.html")
    else:
        return redirect("/")


# 建立 /signout路徑
@app.route("/signout", methods=["GET"])
def signout():
    # print(123)
    # print(session)          # {'id': 'test'}
    session.pop("id", None)
    # print(session)          # {}
    return redirect("/")


# 建立 /error 路徑對應的處理函式
# 錯誤訊息，必須動態的從網址列的 Query String 取得，顯⽰在主畫⾯中。

# /error?message=自訂的錯誤訊息
# message = request.args.get("message", "")
@app.route("/error")
def error():
    message = request.args.get("message")
    # print(message)
    if message == "請輸入帳號、密碼":
        return render_template("error.html", message="請輸入帳號、密碼")
    elif message == "帳號、或密碼輸入錯誤":
        return render_template("error.html", message="帳號、或密碼輸入錯誤")


# 建立 /square/路徑
# 動態路由設定
# /square/某個正整數
@app.route("/square/")
def square():
    num = request.args.get("num")
    # print(num)
    result = int(num)*int(num)
    return render_template("square.html", result=result)


# 啟動網站伺服器， 可透過 port 參數指定埠號
app.run(port=3000)
