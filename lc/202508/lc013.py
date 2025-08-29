table = {
"I" :1,
"IV":4,
"V" :5,
"IX":9,
"X" :10,
"XL":40,
"L" :50,
"XC":90,
"C" :100,
"CD":400,
"D" :500,
"CM":900,
"M" :1000,
}

def roman_to_integer(s):
    i = len(s)
    res = 0
    while i > 1:
        rom = s[i-2:i]
        if rom in table:
            res += table[rom] 
            i -= 2
        else:
            res += table[s[i-1]]
            i -= 1
    if i==1:
        res += table[s[0]]
    return res

            
def roman_to_integer(s):
    i = len(s)
    res = 0
    while i > 1:
        try:
            res += table[s[i-2:i]] 
            i -= 2
        except:
            res += table[s[i-1]]
            i -= 1
    if i==1:
        res += table[s[0]]
    return res


            
