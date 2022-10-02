// 要求一：函式與流程控制
// 完成以下函式，在函式中使用迴圈計算最小值到最大值之間，固定間隔的整數總和。其中你可
// 以假設 max 一定大於 min 且為整數，step 為正整數。

/*
  思考流程:
  1.初始數值為min                             
  2.min隨著每一次迴圈增加1次step           
  3.第一圈停留位置: min                     
	第二圈停留位置 min + step
	第三圈停留位置 min + 2step
  4.迴圈停止的位置不能超過max
  5.計算停留位置的數字加總
  
*/


function calculate(min, max, step){
	let result = 0;
    for(let i = min; i <= max ; i = i + step ){
	// 跑第一圈:result = result + min;                    
	// 跑第二圈:result = result + (min + step) 
	// 跑第三圈:result = result + (min + 2step)
	// console.log(i); 
    result = result + i;
  	}
	console.log(result);

}

calculate(1, 3, 1); // 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2); // 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2); // 你的程式要能夠計算 -1+1，最後印出 0   // 一次走兩步,但不能超過2,只有-1,1





