"""
LC 139 : Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

 

Constraints:

    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.

"""
def wordbreak1(s, wd):
    def helper(start, stop):
        if start >= len(s):
            return True
        if stop > len(s):
            return False
        if s[start:stop] in wd:
            if helper(stop, stop+1):
                return True
        return helper(start, stop+1)
    return helper(0,1)

def wordbreak2(s, wd):
    def helper(start):
        if start >= len(s):
            return True
        if helper(start+1):
            if s[start:start+1] in wd:
                return True
        return helper(start)
    return helper(0)

def wordbreak_dp(s, d):
    results = [False] * len(s)
    for i in range(0, len(s)):
        if s[0:i+1] in d:
            results[i] = True
            continue
        for j in range(i-1, -1, -1):
             if results[j] and s[j+1:i+1] in d:
                results[i] = True
                break
    return results[-1]

# more performant, probably because going backward on j
def wordbreak(s, words):
    n = len(s)+1
    dp = [False] * n
    dp[0] = True
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[-1]


s = "leetcode"
wordDict = ["leet","code"]
print(wordbreak(s, wordDict))
# Output: true

s = "applepenapple"
wordDict = ["apple","pen"]
print(wordbreak(s, wordDict))
# Output: true

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(wordbreak(s, wordDict))
# Output: false
