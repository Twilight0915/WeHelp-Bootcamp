# 要求一：Python 取得網路上的資料並儲存到檔案中
# data.csv 的資料格式
# 根據 xpostDate 欄位，僅輸出 2015 年以後(包含 2015 年) 的資料
# 區域資料 => 地址欄位，三個字

# 景點名稱, 區域, 經度, 緯度, 第一張圖檔網址
# 新北投溫泉區, 北投區, 123.5446, 24.5312, https: // www.travel.taipei/pic/11000848.jpg


import urllib.request as request
import json
import csv

# 串接、擷取公開資料
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)
# 真正需要資料
clist = data["result"]["results"]


# . 步驟:
# . 1. 過濾資料: xpostDate 需大於2015  比較年份大小
# . 2. 修正資料: address  "臺北市  北投區中山路、光明路沿線" => "北投區"
# . 3. 修正資料: file取第一張圖片網址
# . 4. 彙整所有資料輸出到data.csv檔案


# 1.篩選xpostDate Year >= 2015
filterDatas = []

for e in clist:
    # print(e["xpostDate"])          # 2016/07/07
    # 字串切割 取得年分
    filterXpostDate = e["xpostDate"].split("/")
    # print(filterXpostDate)         # ['2016', '07', '07']

    # 比較年分大小 若符合條件則加入 filterDatas (過濾後資料集合)
    if int(filterXpostDate[0]) >= 2015:
        filterDatas.append(e)

# 整理完xpostDate Year >= 2015的資料
# print(filterDatas)


# 2.修正資料: 地區地址、檔案取第一張圖片網址

# 地址篩選陣列
filterAddresses = ["中正區", "萬華區", "中山區", "大同區", "大安區",
                   "松山區", "信義區", "士林區", "文山區", "北投區", "內湖區", "南港區"]


for e in filterDatas:
    # print(e["address"])        # 臺北市  北投區中山路、光明路沿線
    # 地址過濾 僅顯示特定文字
    # 取得地址與篩選陣列核對，是否包含要求區域名稱
    for filterAddress in filterAddresses:
        # print(filterAddress)              # 中正區
        if filterAddress in e["address"]:
            # 更新地址
            e["address"] = filterAddress
    # print(e["address"])                # 北投區

    # 3.file處理
    # print(e["file"])

    # https連結字串異常修正 .jpghttps .jpg https
    e['file'] = e['file'].replace('.jpghttps', '.jpg https')
    # 統一大小寫
    e['file'] = e['file'].replace('.JPG', '.jpg')

    # 檔案取第一張圖片網址
    # 字串切割 找出字串第一個.jpg
    e["file"] = e["file"].split(".jpg")
    # print(e["file"])              # ['https://www.travel.taipei/d_upload_ttn/sceneadmin/pic/11000848', ' https://www.travel.taipei/d_upload_ttn/sceneadmin/pic/11002891',....
    e["file"] = e["file"][0] + ".jpg"
    # print(e["file"])


# 彙整所有資料輸出到data.csv檔案

# 所需資料key值
header = ["stitle", "address", "longitude", "latitude", "file"]

# 寫入至 data.csv
with open("data.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    # 寫入標題行
    # stitle	address	 longitude	 latitude	 firstPicture
    writer.writerow(header)

    # 寫入每行特定資料
    for e in filterDatas:
        row = [e["stitle"], e["address"],
               e["longitude"], e["latitude"], e["file"]]
        writer.writerow(row)
