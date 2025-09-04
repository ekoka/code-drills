"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.

Constraints:
    1 <= tokens.length <= 104
    tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

"""
# backward
def rpn(tokens):
    stack = []
    while tokens:
        t = tokens.pop()
        if t in ops:
            stack.append(t)
            continue
        lft = int(t)
        while stack and stack[-1] not in ops:
            rgt = stack.pop()
            op = ops[stack.pop()]
            lft = op(lft, rgt)
        stack.append(lft)
    return stack[0]
    
ops = {
    '+': lambda op1, op2: op1 + op2,
    '*': lambda op1, op2: op1 * op2,
    '-': lambda op1, op2: op1 - op2,
    '/': lambda op1, op2: int(op1 / op2),
}

# forward
def rpn(tokens):
    stack = []
    for t in tokens:
        if t not in ops:
            stack.append(int(t))
            continue
        op = ops[t]
        rgt = int(stack.pop())
        lft = int(stack.pop())
        stack.append(op(lft, rgt))
    return stack[0]

if __name__=='__main__':
    tokens = ["2","1","+","3","*"]
    exp = 9
    """ Explanation: ((2 + 1) * 3) = 9 """
    res = rpn(tokens)
    print(res)
    assert exp==res


    tokens = ["4","13","5","/","+"]
    exp = 6
    """ Explanation: (4 + (13 / 5)) = 6 """
    res = rpn(tokens)
    print(res)
    assert exp==res

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    exp = 22
    """
    Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22
    """
    res = rpn(tokens)
    print(res)
    assert exp==res

