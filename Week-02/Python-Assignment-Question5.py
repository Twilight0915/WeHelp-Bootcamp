# 要求五：
# Given an array of integers, show indices of the two numbers such that they add up to a
# specific target. You can assume that each input would have exactly one solution, and you
# can not use the same element twice.



def twoSum(nums, target):
  length = len(nums)
  for i in range(length):
    goal = target - nums[i];
    for j in range(length):
      if nums[j] == goal:
        return [i, j]


result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9