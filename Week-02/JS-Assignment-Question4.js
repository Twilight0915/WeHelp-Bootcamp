/*
  要求四：
  找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。  
*/

/*
    思考流程:
    1.排序          // 使用選擇排序法
    2.排序完後，最大兩數和最小兩數乘積進行比較，留下大的

    排序方式:
    1.從小排到大
    2.迴圈第一次找出2出來，但第二次要排除已找出的數字

*/

function maxProduct(nums){

    let length = nums.length;
    // 第一迴圈:數字輪換，每輪一個數字，代表一個數字排好
    for (let i = 0; i < length;i++){
        // 假設nums[i]為最小值，其索引原本為i的位置
        let min = nums[i];
        let minIndex = i;
        // 第二迴圈: 還沒排好的數字進行比較，留下min
        for (let j = i; j < length;j++){
            if(nums[j] < min){
                min = nums[j];
                minIndex = j;
            }
        }
        // 
        // 每完成一個j迴圈，nums原本的序列和數字重新進行排序，接著才進入下個i迴圈
        // *位置交換 
        [nums[minIndex], nums[i]] = [nums[i], nums[minIndex]];
        
    }
    // console.log(nums);    
    // 迴圈完，nums陣列排序完成，找最大兩數乘積和最小兩數乘積進行比較
    let n1 = nums[0]*nums[1]; 
    let n2 = nums[length-1]*nums[length-2]; 
    if (n1 < n2){
        console.log(n2);
    }else{
        console.log(n1);
    }
}

maxProduct([5, 20, 2, 6]); // 得到 120
maxProduct([10, -20, 0, 3]); // 得到 30
maxProduct([10, -20, 0, -3]); // 得到 60
maxProduct([-1, 2]); // 得到 -2
maxProduct([-1, 0, 2]); // 得到 0 或 -0
maxProduct([5, -1, -2, 0]); // 得到 2
maxProduct([-5, -2]); // 得到 10
