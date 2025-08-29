def find_needle(haystack, needle):
    for i in range(len(haystack)):
        if match(haystack, needle, i):
            return i
    return -1

def match(haystack, needle, i):
    if len(haystack) - i < len(needle): return False
    for c in needle:
        if haystack[i]==c:
            i += 1
        else:
            return False
    return True
