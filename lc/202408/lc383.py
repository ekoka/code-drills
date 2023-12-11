"""
LC 383 : Ransom Note

Constraints:
    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.
"""
# 44
# using hashmap
# looks good but not efficient
def can_construct(ransom_note, magazine):
    m = len(ransom_note)
    n = len(magazine)
    if m > n: return False
    letters = {c:0 for s in (ransom_note, magazine) for c in s}
    for l in magazine:
        letters[l] += 1
    for l in ransom_note:
        letters[l] -= 1
    for l,count in letters:
        if count < 0: return False
    return True

# ugly but fairly efficient
def can_construct(ransom_note, magazine):
    m = len(ransom_note)
    n = len(magazine)
    if m > n: return False
    letters = {}
    for l in magazine:
        try:
            letters[l] += 1
        except KeyError:
            letters[l] = 1
    for l in ransom_note:
        try:
            if letters[l]==0: 
                return False
            letters[l] -= 1
        except KeyError:
            return False
    return True

# using str.count()
def can_construct(ransom_note, magazine):
    for c in set(ransom_note):
        if ransom_note.count(c) > magazine.count(c):
            return False
    return True

# using str.index() and str.replace()
def can_construct(ransom_note, magazine):
    for c in ransom_note:
        idx = magazine.index(c)
        if idx==-1:
            return False
        magazine = magazine.replace(c, "", 1)

def can_construct(ransom_note, magazine):
    r_c = {}
    m_c = {}
    for c ransom_note:
        try:
            r_c[c] += 1
        except:
            r_c[c] = 1
    for c in magazine:
        try:
            m_c[c] += 1
        except:
            m_c[c] = 1
    for c in r_c:
        if r_c[c] > m_c[c]: return False
    return True
