# 要求四：
# 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。


def maxProduct(nums):
  length = len(nums)
  for i in range(length):
    minIndex = i
    for j in range(i+1, length):
      if nums[j] < nums[minIndex]:
        minIndex = j
    if minIndex != i:
      nums[i], nums[minIndex] = nums[minIndex], nums[i]
  n1 = nums[0]*nums[1]; 
  n2 = nums[length-1]*nums[length-2]; 
  if n1 < n2:
    print(n2)
  else:
    print(n1)


maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10