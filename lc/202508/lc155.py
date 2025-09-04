"""
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

class MinStack:

    def __init__(self):
        self.values = []
        self.min_values = []

    def push(self, value):
        self.values.append(value)
        if not self.min_values:
            self.min_values.append(value)
            return
        if self.min_values[-1] < value:
            self.min_values.append(self.min_values[-1])
        else:
            self.min_values.append(value)
    
    def pop(self): 
        self.min_values.pop()
        self.values.pop()

    def top(self):
        return self.values[-1]

    def getMin(self):
        return self.min_values[-1]


if __name__=='__main__':
    minStack = MinStack()
    exp = []
    res = minStack.values
    print(res)
    assert exp==res

    minStack.push(-2)
    exp = [-2]
    res = minStack.values
    print(res)
    assert exp==minStack.values

    minStack.push(0)
    exp = [-2, 0]
    res = minStack.values
    print(res)
    assert exp==minStack.values

    minStack.push(-3)
    exp = [-2, 0, -3]
    res = minStack.values
    print(res)
    assert exp==minStack.values

    res = minStack.getMin() 
    exp = -3
    print(res)
    assert exp==res

    res = minStack.pop()
    exp = None
    print(res)
    assert exp==res

    res = minStack.top()
    exp = 0
    print(res)
    assert exp==res

    res = minStack.getMin()
    exp = -2
    print(res)
    assert exp==res

