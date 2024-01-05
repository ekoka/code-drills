"""
LC 155: Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.



Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2



Constraints:

    -231 <= val <= 231 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""
# 04

class MinStack:
    def __init__(self):
        self._stack = []
        self._min = []

    def push(self, item):
        self._stack.append(item)
        if not self._min:
            self._min.append(item)
            return
        if item < self._min[-1]:
            self._min.append(item)
        else:
            self._min.append(self._min[-1])

    def pop(self):
        self._stack.pop()
        self._min.pop()

    def top(self):
        return self._stack[-1]

    def getMin(self):
        return self._min[-1]

"""
Slight optimizations if we combine the stacks.
"""

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        if not self.stack:
            self.stack.append((value, value))
        else:
            self.stack.append(value, min(value, self.stack[-1][1]))

    def pop(self):
        self.stack.pop()
    
    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.min[-1][1]


