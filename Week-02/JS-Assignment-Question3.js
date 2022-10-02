
/*
  要求三：
  完成以下函式，最後能印出程式中註解所描述的結果。
*/



/*
    思考流程:
    1.func(2) => 視為一個變數(函式)
    2.(3,4)的部分  應該是 return b*c
	3.return 回傳值兩個
	4.最後要的結果為 console.log(a+(b*c));
	***從結果逆推思考看看
 */


function func(a){
	return function calculate(b,c){
		// return a+(b*c);
		console.log(a+(b*c));
	};
}

// 驗證:
// let sumNumber = func(2);            // 裝函式的變數
// sumNumber(3,4);                     // 變數();      => 呼叫函式
// console.log(sumNumber);             // calculate函式




func(2)(3, 4); // 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5); // 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9); // 你補完的函式能印出 -3+(2*9) 的結果 15
// 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

