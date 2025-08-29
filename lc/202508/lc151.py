def reverse_words(s):
    words = collect_words(s)
    res = []
    while words:
        res.append(words.pop())
    return ' '.join(res)

def collect_words(s):
    res = []
    word = []
    for c in s:
        if c==' ':
            if word:
                res.append(''.join(word))
                word = []
            continue
        word.append(c)
    if word:
        res.append(''.join(word))
    return res

def reverse_words(s):
    s.append(' ') # ensure all words end with at least one space
    justify(s)
    n = len(s)
    i = 0
    while i < n:
        i = find_char(s, i, n)
        lo = i
        i = find_space(s, i, n)
        hi = i
        rotate_chars(s, lo, hi)
    s.pop()
    rotate_chars(s, 0, n-1)
    return "".join(s)

def rotate_chars(s, first, stop):
    last = stop - 1
    while first < last:
        s[first], s[last] = s[last], s[first]
        first += 1
        last -= 1

def justify(s):
    n = len(s)
    read = 0
    write = 0
    while read < n:
        if s[read]!=' ' or s[read-1]!=' ':
            s[write] = s[read]
            write += 1
        read += 1
    while len(s) > write:
        s.pop()

def find_char(s, i, stop):
    while i < stop:
        if s[i]==' ':
            i += 1
        else:
            break
    return i

def find_space(s, i, stop):
    while i < stop:
        if s[i]==' ':
            break
        i += 1
    return i






s = "the sky is blue"
exp = "blue is sky the"
res = reverse_words(list(s))
print(res)
#assert res==exp

s = "  hello world  "
exp = "world hello"
res = reverse_words(list(s))
print(res)
#assert res==exp

s = "a good   example"
exp = "example good a"
res = reverse_words(list(s))
print(res)
#assert res==exp
