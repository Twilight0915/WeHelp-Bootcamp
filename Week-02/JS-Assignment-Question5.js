/*
要求五：
Given an array of integers, show indices of the two numbers such that they add up to a
specific target. You can assume that each input would have exactly one solution, and you
can not use the same element twice.

翻譯:
任意一串陣列整數，陣列參數對應的兩個數值，可以加總成目標數字，不可以使用同樣資料兩次

*/

/*
    思考流程:
    1.假設let result=twoSum([3, 1, 2], 5);
    2.迴圈: 數字3要與1.2配對
            數字1要與3.2配對
            數字2要與3.1配對
*/


function twoSum(nums, target){
    for(i = 0; i < nums.length;i++){
        let goal = target - nums[i];
        // 數字不可重複
        for(j = i + 1 ; j < nums.length; j++){
            // i = 0, j = 1
            // i = 0, j = 2
            // i = 1, j = 2
            // i = 1, j = 3
            // i = 2, j = 3
            // console.log(i,j)
            if(nums[j] == goal){
                return [i, j];
            }
        }
    }
}

let result=twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9
