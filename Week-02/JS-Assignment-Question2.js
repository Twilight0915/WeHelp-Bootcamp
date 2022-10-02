/*
  要求二：Python 字典與列表、JavaScript 物件與陣列
  完成以下函式，正確計算出非 manager 的員工平均薪資，所謂非 manager 就是在資料中
  manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工，程式需考慮員工資料數量
  不定的情況。
*/

/*
  	思考流程:
	1.data 為物件employees ?
	2.迴圈跑data取出各別資料
	3.比對資料是否為manager
	4.如果manager為false => 取出salary
	5.計算非 manager的salary加總 /非 manager人數

*/ 

function avg(data){
	// console.log(data);
	// console.log(data.employees);
	// console.log(data.employees[0]);
	// console.log(data.employees[0].manager);

	// nm salary total
	let nmSalaryTotal = 0;
	// not manager person number
	let nmPersonNum = 0;

	for (i = 0; i <data.employees.length; i++){
		// console.log(data.employees[i]);
		if(data.employees[i].manager == false){
			// console.log(data.employees[i]);
			// 累加salary
			nmSalaryTotal += data.employees[i].salary;
			// 累加人數
			// 每次迴圈加1
			nmPersonNum += 1;
		}
	}
	// console.log(nmSalaryTotal);
	// console.log(nmPersonNum);
	console.log(nmSalaryTotal/nmPersonNum);
}

avg({
    "employees":[
        {
        "name":"John",
        "salary":30000,
        "manager":false
        },
        {
        "name":"Bob",
        "salary":60000,
        "manager":true
        },
        {
        "name":"Jenny",
        "salary":50000,
        "manager":false
        },
        {
        "name":"Tony",
        "salary":40000,
        "manager":false
        }
    ]
}); // 呼叫 avg 函式



