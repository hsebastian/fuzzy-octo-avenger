"""
http://www.pythonchallenge.com/pc/def/map.html

k -> m
o -> q
e -> g
"""


alpha = [c for c in 'abcdefghijklmnopqrstuvwxyz']
alpha_rotated = [c for c in alpha]
for i in range(2):
    alpha_rotated.reverse()
    alpha_rotated.insert(0, alpha_rotated.pop())
    alpha_rotated.reverse()
print alpha
print alpha_rotated

puzzle_string = (
    "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgl"
    "e gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle"
    " qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
)

answer = ''
for char in puzzle_string:
    print char
    if char.isalpha():
        char_index = alpha.index(char)
        result = alpha_rotated[char_index]
    else:
        result = char
    # print char, answer, result
    answer += result
print answer

# Better solution based on the hint
import string

a = 'abcdefghijklmnopqrstuvwxyz'
b = 'cdefghijklmnopqrstuvwxyzab'
table = string.maketrans(a, b)
print string.translate(puzzle_string, table)
print string.translate('map', table)

