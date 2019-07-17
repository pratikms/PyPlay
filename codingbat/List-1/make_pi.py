# Problem Statement
# 
# 
# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
# 
# 
# make_pi() → [3, 1, 4]

def make_pi():
    import math
    return [int(num) for num in str(int(math.pi * 100))]

print(make_pi())