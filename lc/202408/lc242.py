"""
LC 242 : Valid Anagram
"""
# 54 - 58 (solved)
def is_anagram(s, t):
    if len(s)!=len(t): return False
    for c in s:
        t = t.replace(c, "", 1)
    return t==""

def is_anagram(s, t):
    if len(s)!=len(t): return False
    match = {c:0 for c in string for string in (s,t)}
    for c in s: 
        match[c] += 1
    if not all(match.values()):
        return False
    for c in t:
        match[c] -= 1 
    return not any(match.values())

# fairly efficient
def is_anagram(s, t):
    if len(s)!=len(t): 
        return False
    match = {c:0 for string in (s,t) for c in string}
    for c in s: 
        match[c] += 1
    for c in t:
        match[c] -= 1 
    for v in match.values():
        if v: return False
    return not any(match.values())
