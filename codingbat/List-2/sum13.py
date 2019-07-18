# Problem Statement
# 
# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
# 
# 
# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6

def sum13(nums):
    try:
        index = nums.index(13)
    except Exception:
        index = len(nums)
    finally:
        return sum([nums[idx] for idx in range(index)])

print(sum13([1, 2, 2, 1]))
print(sum13([1, 1]))
print(sum13([1, 2, 2, 1, 13]))