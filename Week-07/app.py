from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
# 使用 mysql-connector-python 套件連結資料庫
import mysql.connector


# jsonify() 函數輸出為 JSON 格式
from flask import jsonify

# 建立 Application 物件，設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)
# 更改JSON字典格式的無序性
app.config['JSON_SORT_KEYS'] = False

# 設定session密鑰
app.secret_key = "Week-06 assignment"

# 連結website資料庫
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
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


# 建立查詢會員資料的 API
# Query String 要求字串：username=要查詢的會員帳號
# URL Example 呼叫範例：http://127.0.0.1:3000/api/member?username=ply
@app.route("/api/member", methods=["GET", "PATCH"])
def api_member():
    if request.method == "GET":
        username = request.args.get("username", "")
        # print(username)              # 前端的 input button都要包覆在form裡面,username才會隨著按鈕送入後端

        # member資料
        sql = "SELECT * FROM member WHERE username=%s"
        val = [username]
        cursor.execute(sql, val)
        member_data = cursor.fetchone()
        # print(member_data)
        # (2, 'Tom', 'apple', 'red', 40, datetime.datetime(2022, 10, 23, 20, 18, 40))

        # 沒有資料會是null
        # fetchall()
        # [ [資料1],[資料2],[資料3],[資料4],[資料5] ]
        # return jsonify(member_data)

        # {} 是無序的

        if member_data != None:
            return jsonify(
                {
                    "data": {
                        "id": member_data[0],
                        "name": member_data[1],
                        "username": member_data[2]
                        # "password": member_data[3],
                        # "follower_count": member_data[4],
                        # "time": member_data[5]
                    }
                }
            )
        else:
            return jsonify(
                {
                    "data": member_data}
            )
    elif request.method == "PATCH":

        # 取得要求數據request.data
        # 取得json型式數據  request.json()

        # name_update = request.data
        # print(name_update)
        # b'{"data":{"name":"\xe6\xb9\xaf\xe7\xb1\xb3"}}'

        # patch送過來json型態資料
        data = request.json
        # print(data)        # {'data': {'name': '湯米'}}

        name_update = data["data"]["name"]
        # print(name_update)                  # 湯米

        # 回應格式
        payload_true = {
            "OK": "true"
        }
        payload_error = {
            "error": "true"
        }

        # 未更新前 session狀態
        # print(session["name"])         # Tom
        name = session["name"]
        id = session["id"]
        # print(session["id"])           # 2

        # 目前登入者，資料庫中 "name": "Tom"   => "name":  "湯米"
        # sql_1 = "SELECT * FROM member WHERE id = %s"
        # val_1 = [id]
        # cursor.execute(sql_1, val_1)
        # member_data = cursor.fetchone()
        # print(member_data)
        # (2, 'Tom', 'apple', 'red', 40, datetime.datetime(2022, 10, 23, 20, 18, 40))

        # 資料庫更新
        # 目前登入者，資料庫中 "name": "Tom"   => "name":  "湯米"
        sql_2 = "UPDATE member SET name = %s WHERE id = %s "
        val_2 = (name_update, id)
        cursor.execute(sql_2, val_2)
        # 抓取sql執行完的回傳值
        result = cursor.fetchone()
        # print(result)               # None 空值
        db.commit()

        # 新的name資料
        # sql_3 = "SELECT * FROM member WHERE name=%s AND id=%s "
        # val_3 = (name_update, id)
        # cursor.execute(sql_3, val_3)
        # new_member_data = cursor.fetchone()
        # print(new_member_data)
        # (2, '湯米', 'apple', 'red', 40, datetime.datetime(2022, 10, 23, 20, 18, 40))

        # 更新狀況回應給前端。
        # 更新成功，資料庫可以找到符合 new_member_data 資料
        # if new_member_data[1] != None:
        #     # 更新session["name"]，更改為name_update
        #     session["name"] = name_update
        #     return jsonify(payload_true)
        # else:
        #     # 更新失敗
        #     return jsonify(payload_error)

        if result == None:
            session["name"] = name_update
            return jsonify(payload_true)
        else:
            return jsonify(payload_error)

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
