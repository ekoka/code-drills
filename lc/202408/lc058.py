# 02 - 08
"""
Constraints:
    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.
"""
def length_last_word(s):
    i = len(s)-1
    while i==" ":
        i -= 1

    j = i
    while j >= 0 and j!=" ":
        j -= 1

    return i - j

    
