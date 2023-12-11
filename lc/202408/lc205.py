"""
LC 205 : Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:

    Mapping 'e' to 'a'.
    Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "title"
Output: true
 

Constraints:
    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.
"""
# 43 - 54 
def is_isomorphic(s, t):
    s_to_t = {}
    t_to_s = {}
    for i in range(len(s)):
        if s[i] in s_to_t: 
            if t[i]!=s_to_t[s[i]]:
                return False
        else:
            s_to_t[s[i]] = t[i]
        if t[i] in t_to_s: 
            if s[i]!=t_to_s[t[i]]:
                return False
        else:
            t_to_s[t[i]] = s[i]
    return True

def is_isomorphic(s, t):
    s_to_t = {}
    t_to_s = {}
    for i in range(len(s)):
        if s[i] in s_to_t: 
            if t[i]!=s_to_t[s[i]]:
                return False
        else:
            s_to_t[s[i]] = t[i]
        if t[i] in t_to_s: 
            if s[i]!=t_to_s[t[i]]:
                return False
        else:
            t_to_s[t[i]] = s[i]
    return True

# using find
def is_isomorphic(s, t):
    for i in range(len(s)):
        sidx = s.find(s[i])
        tidx = t.find(t[i])
        if sidx!=tidx:
            return False
    return True

# derived from the above (efficiency swings between 57% and 96%)
def is_isomorphic(s, t):
    sidx = {}
    tidx = {}
    for i in range(len(s)):
        sidx[s[i]] = i 
        tidx[t[i]] = i
    for i in range(len(s)):
        if sidx[s[i]]!=tidx[t[i]]:
            return False
    return True

def is_isomorphic(s, t):
    sidx = {}
    tidx = {}
    for i in range(len(s)):
        sidx[s[i]] = i 
        tidx[t[i]] = i
    return all([sidx[s[i]]==tidx[t[i]] for i in range(len(s))])

def is_isomorphic(s, t):
    sidx = {}
    tidx = {}
    N = len(s)
    i = 0
    while i < N:
        sidx[s[i]] = i 
        tidx[t[i]] = i
        i += 1
    res = True
    i = 0
    while res and i < N: 
        res = sidx[s[i]]==tidx[t[i]]
        i += 1
    return res
# seems more consistently efficient
def is_isomorphic(s, t):
    sidx = {}
    tidx = {}
    N = [i for i in range(len(s))]
    for i in N:
        sidx[s[i]] = i 
        tidx[t[i]] = i
    res = True
    for i in N: 
        res = sidx[s[i]]!=tidx[t[i]]
    return res

