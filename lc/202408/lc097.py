"""
LC 097 : Interleaving Strings

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m
substrings
respectively, such that:

    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:

    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1, s2, and s3 consist of lowercase English letters.

Follow up: Could you solve it using only O(s2.length) additional memory space?
"""
def is_interleave1(s1, s2, s3):
    def helper(i, j, k):
        c = s3[k]
        if i==len(s1): 
            return s2[j:]==s3[k:]
        if j==len(s2): 
            return s1[i:]==s3[k:]
        if s1[i]==c and helper(i+1, j, k+1):
            return True
        elif s2[j]==c and helper(i, j+1, k+1):
            return True
        return False
    return helper(0, 0, 0)

def is_interleave_dp1(s1, s2, s3):
    if len(s1)+len(s2)!=len(s3): return False
    results = [ [False] * (len(s2) + 1) for _ in range(len(s1)+1)]
    results[0][0] = True
    for i in range(1, len(s1)+1):
        results[i][0] = results[i-1][0] and s1[i-1]==s3[i-1]
        if not results[i][0]:
            break
    for j in range(1, len(s2)+1):
        results[0][j] = results[0][j-1] and s2[j-1]==s3[j-1]
        if not results[0][j]:
            break

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            c = s3[i+j-1]
            results[i][j] = ((results[i-1][j] and s1[i-1]==c) 
                              or (results[i][j-1] and s2[j-1]==c))
    return results[-1][-1]

def is_interleave_dp2(s1, s2, s3):
    if len(s1)+len(s2)!=len(s3): 
        return False
    if len(s2)==0:
        return s1==s3
    if len(s1)==0:
        return s2==s3

    results = [ [False] * (len(s2) + 1) for _ in range(2)]
    results[0][0] = True
    for j in range(1, len(s2)+1):
        results[0][j] = results[0][j-1] and s2[j-1]==s3[j-1]
        if not results[0][j]:
            break
    results[1][0] = results[0][0] and s1[0]==s3[0]

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            c = s3[i+j-1]
            results[1][j] = ((results[0][j] and s1[i-1]==c)
                              or (results[1][j-1] and s2[j-1]==c))
        results[0], results[1] = results[1], results[0]
        results[1][0] = False

    return results[0][-1]

def is_interleave_dp3(s1, s2, s3):
    if len(s1)+len(s2)!=len(s3): return False
    if len(s2)==0: return s1==s3 # not necessary
    if len(s1)==0: return s2==s3 # not necessary

    n1 = len(s1) + 1
    n2 = len(s2) + 1

    prev = [False] * n2
    curr = [False] * n2 # this is not actually needed (see next solution)
    prev[0] = True
    for j in range(1, n2):
        prev[j] = prev[j-1] and s2[j-1]==s3[j-1]
        if not prev[j]: # Premature optimization. Actually costs an extra check at each loop.
            break

    for i in range(1, n1):
        curr[0] = prev[0] and s1[i-1]==s3[i-1]
        for j in range(1, n2):
            c = s3[i+j-1]
            curr[j] = ((prev[j] and s1[i-1]==c) or (curr[j-1] and s2[j-1]==c))
        prev, curr = curr, prev 
    return prev[-1]

def is_interleave_dp4(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3): return False

    dp = [False] * (len(s2) + 1)
    dp[0] = True

    for j in range(1, len(s2)+1):
        dp[j] = dp[j-1] and s2[j-1]==s3[j-1]

    for i in range(1, len(s1)+1):
        dp[0] = dp[0] and s1[i-1]==s3[i-1]
        for j in range(1, len(s2)+1):
            dp[j] = ((dp[j] and s1[i-1]==s3[i+j-1]) or (dp[j-1] and s2[j-1]==s3[i+j-1]))
    return dp[-1]

