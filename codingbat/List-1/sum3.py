# Problem Statement
# 
# Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
# 
# sum3([1, 2, 3]) → 3
# sum3([1, 1]) → 2
# sum3([1, 1, 1, 1]) → 2

def sum3(nums):
    return nums[0] + nums[1] if len(nums) >= 2 else nums[0] if len(nums) > 0 else 0

print(sum3([1, 2, 3]))
print(sum3([1, 1]))
print(sum3([1, 1, 1, 1]))
print(sum3([3]))
print(sum3([]))