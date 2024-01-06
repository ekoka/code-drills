"""
LC 150: Evaluate Reverse Polish Notation

You are given an array of strings `tokens` that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:

    1 <= tokens.length <= 104
    tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""
# 50 -
# front to back
ops = {
    '/': lambda l,r: int(l/r), '*': lambda l,r: l*r,
    '+': lambda l,r: l+r, '-': lambda l,r: l-r, }

def eval_rpn(tokens):
    stack = []
    for t in tokens:
        if t in ops:
            r = stack.pop()
            l = stack.pop()
            stack.append(ops[t](l, r))
            continue
        stack.append(int(t))
    return stack[-1]


# back to front
def eval_rpn(tokens):
    stack = []
    while tokens:
        t = tokens.pop()
        if t in ops:
            stack.append(t)
            continue
        t = int(t)
        while stack and stack[-1] not in ops:
            r = stack.pop()
            o = ops[stack.pop()]
            t = o(int(t), r)
        stack.append(t)
    return stack[0]

tokens = ["2","1","+","3","*"]
print(eval_rpn(tokens))
# Output: 9

tokens = ["4","13","5","/","+"]
print(eval_rpn(tokens))
# Output: 6

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(eval_rpn(tokens))
# Output: 22
