# Problem Statement
# 
# 
# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
# 
# 
# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4

def sum67(nums):
    try:
        section_start = nums.index(6)
        section_end = nums.index(7) + 1
    except Exception:
        section_start = 0
        section_end = 0
    finally:
        generated_nums = nums[:section_start]
        generated_nums.extend(nums[section_end:])
        return sum(generated_nums)

print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))