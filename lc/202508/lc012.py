ints = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
rom =  [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]

def int_to_rom(num):
    res = []
    i = 0
    while num > 0:
        if num < ints[i]:
            i += 1
        else:
            num -= ints[i]
            res.append(rom[i])
    return "".join(res)


def int_to_rom(num):
    ints = [ 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900 ]
    rom =  [ "I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM" ]
    i = 1000
    r = "M"
    res = []
    while num > 0:
        if num < i:
            i = ints.pop()
            r = rom.pop()
            continue
        num -= i
        res.append(r)
    return res
