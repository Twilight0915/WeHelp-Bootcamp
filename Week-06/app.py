from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
# 使用 mysql-connector-python 套件連結資料庫
import mysql.connector


# 建立 Application 物件，設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

# 設定session密鑰
app.secret_key = "Week-06 assignment"

# 連結website資料庫
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="website"
)
# 對資料庫進行操作
# 使用指標  cursor()
cursor = db.cursor()


# 建立路徑 / 對應的處理函式
@app.route("/")
def index():
    return render_template("index.html")


# 註冊帳號
# 建立路徑 / signup
# 使用 POST方法
@app.route("/signup", methods=["POST"])
def signup():
    # 接收前端輸入的資料
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]

    # 檢查資料庫的 member 資料表中是否有重複的 username

    # member資料表欄位名稱
    # id, name, username, password, follower_count, time

    # 檢查資料庫的 member 資料表中是否有重複帳號的資料
    sql_1 = "SELECT * FROM member WHERE username=%s"
    #  Could not process parameters: str(apple), it must be of type list, tuple or dict
    val_1 = [username]

    cursor.execute(sql_1, val_1)
    # 有重複才會搜到東西
    check_user = cursor.fetchone()
    # print(check_user)    # ('apple',)

    # 註冊成功，導回首頁
    if check_user == None:
        # print(check_user)
        sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        val = (name, username, password)
        cursor.execute(sql, val)
        db.commit()
        return redirect("/")
    else:
        return redirect("/error?message=帳號已經被註冊")


# 登入帳號
# 建立路徑 / signin
# 使用 POST方法
@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]

    # 執行: 查詢 member資料表，是否有符合 輸入username及password的資料
    sql_2 = "SELECT * FROM member WHERE username=%s and password=%s"
    val_2 = (username, password)
    cursor.execute(sql_2, val_2)

    login_user = cursor.fetchone()
    # print(login_user)
    # (2, 'Tom', 'apple', 'red', 40, datetime.datetime(2022, 10, 23, 20, 18, 40))
    if login_user != None:
        id = login_user[0]
        name = login_user[1]
        session["id"] = id
        session["name"] = name
        # print(session)                   # <SecureCookieSession {'id': 2, 'name': 'Tom'}>
        return redirect("/member")
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")


# 建立 /member路徑對應的處理函式
@app.route("/member")
def member():
    # print(session["name"])             # Tom
    if "name" in session:                # 檢測session{} 裡面有沒有name這個 key
        name = session["name"]
        return render_template("member.html", name=name)
    else:
        return redirect("/")


# 建立 /signout路徑
@app.route("/signout", methods=["GET"])
def signout():
    # print(session)          #  {'id': 2, 'name': 'Tom'}>
    session.clear()
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
    if message == "帳號、或密碼輸入錯誤":
        return render_template("error.html", message="帳號、或密碼輸入錯誤")
    elif message == "帳號已經被註冊":
        return render_template("error.html", message="帳號已經被註冊")


# 啟動網站伺服器， 可透過 port 參數指定埠號
app.run(port=3000)
