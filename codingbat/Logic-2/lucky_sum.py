# Problem Statement
# 
# 
# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
# 
# 
# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1

def lucky_sum(a, b, c):
    try:
        collection = [a, b, c]
        count = collection.index(13)
    except Exception as error:
        count = len(collection)
    finally:
        return sum([collection[index] for index in range(count)])

print(lucky_sum(1, 2, 3))
print(lucky_sum(1, 2, 13))
print(lucky_sum(1, 13, 3))