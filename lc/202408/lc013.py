"""
LC 013 : Roman Integers


I             1
V             5
X             10
L             50
C             100
D             500
M             1000
IV            4
IX            9
XL            40
XC            90
CD            400
CM            900


Constraints:

    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999]
"""
# 54
table = {
    "I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000,
    "IV": 4, "IX": 9, "XL": 40,
    "XC": 90, "CD": 400, "CM": 900,
}

def rom_to_int(s):
    n = len(s)
    i = 0
    num = 0
    while i < n:
        if i < n-1 and s[i:i+2] in table:
            c = s[i:i+2]
            i += 2
        else:
            c = s[i]
            i += 1
        num += table[c]
    return num
