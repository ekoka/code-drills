"""
LC 290 : Word Pattern

Constraints:
    1 <= pattern.length <= 300
    pattern contains only lower-case English letters.
    1 <= s.length <= 3000
    s contains only lowercase English letters and spaces ' '.
    s does not contain any leading or trailing spaces.
    All the words in s are separated by a single space.
"""
# 43 
def word_pattern(pattern, s): 
    s = s.split()
    len(s) = N
    if len(pattern)!=N: return False
    
    I = [i for i in range(N)]
    pidx = {}
    sidx = {}
    for i in I:
        sidx[s[i]] = i
        pidx[pattern[i]] = i
    for i in I:
        if pidx[pattern[i]]!=sidx[s[i]]:
            return False
    return True



    


