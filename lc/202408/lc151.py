"""
LC 151 : Reverse Words in a String

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.



Constraints:

    1 <= s.length <= 104
    s contains English letters (upper-case and lower-case), digits, and spaces ' '.
    There is at least one word in s.

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""
# 13 - 36
# follow up 16 (~1h)
#def solution(s):
#    left_justify(s)
#    left_trim(s)
#    reverse(s, 0, len(s))
#    for start, stop in parse_words(s):
#        reverse(s, start, stop)
#
#def left_justify(s):
#    scan = record = 0
#    padding = False
#    while scan < len(s):
#        value = s[scan]
#        s[scan] = ' '
#        if value==' ':
#            scan += 1
#            if padding:
#                s[record] = value
#                record += 1
#                padding = False
#            continue
#        padding = True
#        s[record] = value
#        scan += 1
#        record += 1
#
#
#def parse_words(s):
#    start = 0
#    stop = 0
#    rv = []
#    while start < len(s):
#        start = parse_start(s, start)
#        if start >= len(s): break
#        stop = parse_stop(s, start)
#        rv.append((start, stop))
#        start = stop
#    return rv
#
#def parse_start(s, start):
#    while start < len(s) and s[start]==' ':
#        start += 1
#    return start
#
#def parse_stop(s, start):
#    stop = start + 1
#    while stop < len(s) and s[stop]!=' ':
#        stop += 1
#    return stop

#def array_swap(array, i, j):
#    array[i], array[j] = array[j], array[i]
#

# non-mutating
def reverse(s):
    res = []
    for st, sp in words(s):
        res.append(s[st:sp])
    return ' '.join(res)

def words(s):
    res = []
    n = len(s)
    sp = n
    for i in range(n-1, -2, -1):
        if i==-1 or s[i]==' ':
            if i < n-1 and s[i+1]!=' ':
                res.append((i+1, sp))
            sp = i
    return res

# in-place
def justify(s):
    j = 0
    parsing = False
    for i in range(len(s)):
        if s[i]==' ':
            parsing = False
            continue
        if j>0 and not parsing:
            s[j] = ' '
            j += 1
        parsing = True
        s[j] = s[i]
        j += 1
    return j

def crop(s, start):
    n = len(s)
    while start < n:
        s.pop()
        start += 1

def reverse(s):
    n = justify(s)
    crop(s, n)
    slice_reverse(s, 0, n)
    for st, sp in words(s):
        slice_reverse(s, st, sp)
    return s

def slice_reverse(arr, start, stop):
    while start < stop:
        array_swap(arr, start, stop-1)
        start += 1
        stop -= 1

def array_swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def words(s):
    res = []
    st = 0 # start
    for i in range(len(s)+1):
        if i==len(s) or s[i]==' ':
            if s[i-1]!=' ':
                res.append((st, i))
            st = i+1
    return res

#s = "the sky is blue"
s = list("the sky is blue")
print(reverse(s))
print(s)
assert s==list("blue is sky the")

#s = "  hello world  "
s = list("  hello world  ")
print(reverse(s))
print(s)
assert s==list("world hello")

#s = "a good   example"
s = list("a good   example")
print(reverse(s))
print(s)
assert s==list("example good a")


"""
Insights:
- the slice_reversal() algorithm is easier with the approach of incrementing `start` while decrementing `stop`.
- the justify() algorithm is deceptive. Just keep things simple and stupid when implementing it, otherwise you could spend a long time on it trying to make it clever.
- the words() algorithm seems to need `start` and `stop` variables, but actually only one is needed, the `i` counter is used to record the other position.
"""
