# 要求二：Python 字典與列表、JavaScript 物件與陣列
# 完成以下函式，正確計算出非 manager 的員工平均薪資，所謂非 manager 就是在資料中
# manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工，程式需考慮員工資料數量
# 不定的情況。

def avg(data):
  # 抓出所有manager == False 的員工
  # 迴圈跑每一個員工的資料
  # data => dictionary字典        # dict[key] = value   
  # data["employees"] 
  # 平均薪資 = 總薪資/人數
  nmSalaryTotal = 0 
  nmPersonNum = 0
  # 每一迴圈i代入一個員工
  for i in data["employees"]:
    if i["manager"] == False:
      nmSalaryTotal = nmSalaryTotal + i["salary"]
      nmPersonNum = nmPersonNum + 1
  print(nmSalaryTotal/nmPersonNum)


avg({
"employees":[
{
"name":"John",
"salary":30000,
"manager":False
},
{
"name":"Bob",
"salary":60000,
"manager":True
},
{
"name":"Jenny",
"salary":50000,
"manager":False
},
{
"name":"Tony",
"salary":40000,
"manager":False
}
]
}) # 呼叫 avg 函式