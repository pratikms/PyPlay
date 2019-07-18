# Problem Statement
# 
# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
# 
# 
# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False

def has22(nums):
    try:
        first_occurrence = nums.index(2)
        second_occurrence = first_occurrence + 1
    except Exception:
        pass
    finally:
        return nums[first_occurrence] == 2 and nums[second_occurrence] == 2

print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))
print(has22([2, 1, 2]))