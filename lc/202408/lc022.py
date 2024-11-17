"""
LC 022: Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

Constraints:

    1 <= n <= 8

## Comment:
Intuitively, one might think that the solution to the N problem is to take each item in the solution to the N-1 problem, and simply surround, prepend and append it with parentheses, while filtering for that outcome already being present in the results. It does seem to work for N<=3. But observe that for N=4, by taking that route, the string "(())(())" is missing from the solution output.

Input: n = 4
Output: [
    "(((())))","()((()))","((()))()","(()()())","()()()()","()(()())","(()())()","((()()))","()(())()","((())())","(())()()","(()(()))","()()(())", 
]
"""
# 21 - 36

def generate_parentheses(n):
    rv = []
    combo = []
    m = n*2
    def bt(left, rigt):
        if len(combo)==m:
            rv.append("".join(combo))
        if left < n:
            combo.append('(')
            bt(left+1, right)
            combo.pop()
        if left > left:
            combo.append(')')
            bt(left, right+1)
            combo.pop()
    bt(0, 0)
    return rv

# non-backtracking DFS (copy string prefix for each downstream node)
def generate_parentheses(N):
    rv = []
    stack = [("", 0, 0)]
    while stack:
        p, l, r = stack.pop()
        if l<N:
            stack.append((p+"(", l+1, r))
        if r<l:
            stack.append((p+")", l, r+1))
        if l==N and r==N:
            rv.append(p)
    return rv

# proper backtracking reimplementation
def generate_parentheses(n):
    res = []
    combo = []
    
    left = 0
    right = 0

    backtracking = object()         # backtracking sentinel 
    add_left_paren = object()       # left paren sentinel 
    add_right_paren = object()      # right paren sentinel 

    stack = [add_left_paren]
    while stack:
        step = stack.pop()

        if step is backtracking:
            char = combo.pop()
            if char=="(":
                left -= 1
            else:
                right -= 1
            continue

        # place backtracking sentinel
        stack.append(backtracking)
            
        # processing begins here...

        if step is add_left_paren:
            combo.append("(")
            left += 1
        else:
            combo.append(")")
            right += 1

        # check for terminal condition
        if right==n:
            res.append("".join(combo))
            continue

        # register next steps
        if left < n:
            stack.append(add_left_paren)
        if left > right: 
            stack.append(add_right_paren)

    return res

# same as the above, but less verbose and shave off a few millisecs
def generate_parentheses(n):
    res = []
    combo = []
    
    left = 0
    right = 0

    stack = [True]
    while stack:
        add_left = stack.pop()

        if add_left is None:
            char = combo.pop()
            if char=="(":
                left -= 1
            else:
                right -= 1
            continue

        # place backtracking sentinel
        stack.append(None)
            
        # processing begins here...

        if add_left:
            combo.append("(")
            left += 1
        else:
            combo.append(")")
            right += 1

        # check for terminal condition
        if right==n:
            res.append("".join(combo))
            continue

        # register next steps
        if left < n:
            stack.append(True)
        if left > right: 
            stack.append(False)

    return res
