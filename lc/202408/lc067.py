"""
LC 067 : Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Constraints:

    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.

"""
"11"
"1"

"""
xor:
    1 ^ 1 = 0
    1 ^ 0 = 1
    0 ^ 1 = 1
    0 ^ 0 = 0
"""
def binadd(a, b):
    a = list(a)
    b = list(b)
    carry = False
    res = []
    while a and b:
        v1 = a.pop()=="1"
        v2 = b.pop()=="1"
        if carry:
            if v1:
                v1 = False
            else:
                v1 = True
                carry = False
        if v1:
            if v2:
                res.append("0")
                carry = True
            else:
                res.append("1")
        else:
            if v2:
                res.append("1")
            else:
                res.append("0")

    c = a or b
    while c:
        v = c.pop()=="1"
        if carry:
            if v:
                v = False
            else:
                v = True
                carry = False
        res.append("1" if v else "0")
    if carry:
        res.append("1")
    return "".join(reversed(res))

