# Problem Statement
# 
# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
# 
# 
# combo_string('Hello', 'hi') → 'hiHellohi'
# combo_string('hi', 'Hello') → 'hiHellohi'
# combo_string('aaa', 'b') → 'baaab'

def combo_string(a, b):
    if len(a) <= len(b):
        shorter_string, longer_string = a, b
    else:
        shorter_string, longer_string = b, a
    return f'{shorter_string}{longer_string}{shorter_string}'

print(combo_string('Hello', 'hi'))
print(combo_string('hi', 'Hello'))