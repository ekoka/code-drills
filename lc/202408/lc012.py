"""
LC 012 : Integer to Roman

Seven different symbols represent Roman numerals with the following values:

    Symbol	Value
    I	    1
    V	    5
    X	    10
    L	    50
    C	    100
    D	    500
    M	    1000

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

- If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
- If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
- Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.

Given an integer, convert it to a Roman numeral.

Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII

Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV

Constraints:

    1 <= num <= 3999

"""
# 50
def dec_to_rom(value):
    def helper(v):
        pv = extract_maxpower_value(v)
        rv = [to_roman(pv)]
        if v - pv > 0:
            rv.append(helper(v-pv))
        return "".join(rv)
    return helper(value)

def to_roman(v):
    if v >= 1000:
        return to_thousands(v)
    if v >= 100:
        return to_hundreds(v)
    if v >= 10:
        return to_tens(v)
    return to_units(v)

def to_units(v):
    if v==4:
        return 'IV'
    if v==9:
        return 'IX'
    prefix = ''
    if v>=5:
        prefix = 'V'
        v -= 5
    units = 1
    count = 0
    while v >= units:
        count += 1
        units += 1
    return prefix + ('I' * count)

def to_tens(v):
    if v==40:
        return 'XL'
    if v==90:
        return 'XC'
    prefix = ''
    if v>=50:
        prefix = 'L'
        v -= 50
    tens = 10
    count = 0
    while v >= tens:
        count += 1
        tens += 10
    return prefix + ('X' * count)

def to_hundreds(v):
    if v > 1000:
        raise Exception('Invalid hundred value')
    if v==400:
        return 'CD'
    if v>=900:
        return 'CM'
    prefix = ''
    if v >= 500:
        prefix = 'D'
        v -= 500
    hundreds = 100
    count = 0
    while v >= hundreds:
        count += 1
        hundreds += 100
    return prefix + ('C' * count)

def to_thousands(v):
    thousands = 1000
    count = 0
    while v >= thousands:
        count += 1
        thousands += 1000
    return 'M' * count

def extract_maxpower_value(value):
    lo = 1
    hi = 10
    rv = 0
    while hi < value:
        lo *= 10
        hi *= 10
    while value >= lo:
        value -= lo
        rv += lo
    return rv

assert extract_maxpower_value(3749)==3000
assert extract_maxpower_value(9)==9
assert extract_maxpower_value(58)==50
assert extract_maxpower_value(1994)==1000
assert to_thousands(3749)=='MMM'
assert to_thousands(2000)=='MM'
assert to_thousands(1000)=='M'
assert to_hundreds(749)=='DCC'
assert to_hundreds(500)=='D'

def int_to_rom(num):
    int_rom = [(1000, 'M'), (900,'CM'), (500, 'D'), (400, 'CD'), (100,'C'), (90, 'XC'),
               (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    i = 0
    res = []
    while num:
        if num < int_rom[i][0]:
            i += 1
            continue
        res.append(int_rom[i][1])
        num -= int_rom[i][0]
    return ''.join(res)

num = 3749
rv = int_to_rom(num)
print(rv)
assert rv=="MMMDCCXLIX"

num = 58
rv = int_to_rom(num)
print(rv)
assert rv=="LVIII"

num = 1994
rv = int_to_rom(num)
print(rv)
assert rv=="MCMXCIV"

"""
Insight: Sometimes the key to the solution is to complete the data structure. Instead of coding the intricate logic to identify 4 and 9 values, we just added them to the original set. It made for a much simpler solution.
"""
