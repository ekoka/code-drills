"""
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Constraints:
    1 <= n <= 231 - 1
"""
def is_happy(n):
    visited = set()
    while n!=1:
        if n in visited: return False
        nxt_n = sum(int(d)**2 for d in str(n))
        visited.add(n)
        n = nxt_n
    return True

if __name__=='__main__':
    n = 19
    exp = True
    res = is_happy(n)
    print(res)
    assert exp==res
    """
    Explanation:
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1
    """

    n = 2
    exp = False
    res = is_happy(n)
    print(res)
    assert exp==res
