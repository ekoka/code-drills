"""
LC 020 : Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""
# 50 - 11 (100%) - 17 (clean up)
def is_valid(s):
    brackets = {"(":")", "[":"]", "{":"}"}
    stack = []
    for i in range(len(s)):
        b = s[i]
        if not stack:
            if b not in brackets:
                return False
            stack.append(b)
            continue
        if b in brackets:
            stack.append(b)
            continue
        if  b!=brackets[stack.pop()]:
            return False
    return len(stack)==0

def is_valid(s):
    brackets = {"(":")", "[":"]", "{":"}"}
    stack = []
    for i in range(len(s)):
        b = s[i]
        if b in brackets:
            stack.append(b)
        elif not stack or b!=brackets[stack.pop()]:
            return False
    return len(stack)==0
