"""
LC 173: Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/description/

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class.

The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.

boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.

int next() Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.



Example 1:

Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False

Constraints:

    The number of nodes in the tree is in the range [1, 105].
    0 <= Node.val <= 106
    At most 105 calls will be made to hasNext, and next.

Follow up:

Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?
"""
from .bt import maketree

class BSTIterator:
    """
    Classic traversal. Ok performance with type hinting.
    """
    def __init__(self, root):
        self.stack = [root]
        self._next = root.left

    def next(self) -> int:
        while self.stack or self._next:
            if self._next:
                self.stack.append(self._next)
                self._next = self._next.left
            else:
                n = self.stack.pop()
                self._next = n.right
                return n.val

    def hasNext(self) -> bool:
        return bool(self.stack or self._next)

class BSTIterator: 
    """
    Using an alternative iterative traversal strategy. Does require full traversal prior to 
    output. Decent performance (mostly due to type hinting), but traverses the entire tree, before outputting.
    """
    def __init__(self, root: TreeNode):
        self.cur = -1
        self.iot = []
        stack = []
        next = root
        while next:
            while next:
                stack.append(next)
                next = next.left
            while stack:
                n = stack.pop()
                self.iot.append(n.val)
                if n.right:
                    next = n.right
                    break

    def next(self) -> TreeNode:
        self.cur += 1
        return self.iot[self.cur]

    def hasNext(self) -> bool:
        return self.cur + 1 < len(self.iot)

class BSTIterator:
    """
    Very good performance due to splitting discovery and output phases.
    Added performance boost from type hinting.
    """
    def __init__(self, root):
        self.iot = []
        self.add_left_most(root)

    def add_left_most(self, node):
        while node:
            self.iot.append(node)
            node = node.left

    def next(self):
        n = self.iot.pop()
        self.add_left_most(n.right)
        return n.val

    def has_next(self):
        return len(self.iot) > 0

class BSTIterator: 
    """
    Using an alternative iterative traversal strategy. Does require full traversal prior to 
    output. Decent performance.
    """
    def __init__(self, root: TreeNode):
        self.cur = -1
        self.iot = []
        stack = []
        next = root
        while next:
            while next:
                stack.append(next)
                next = next.left
            while stack:
                n = stack.pop()
                self.iot.append(n.val)
                if n.right:
                    next = n.right
                    break

    def next(self) -> TreeNode:
        self.cur += 1
        return self.iot[self.cur]

    def hasNext(self) -> bool:
        return self.cur + 1 < len(self.iot)


class BSTIterator: 
    """
    Adapted from above, but using a generator. Decent performance with type hinting (70%).
    """
    def __init__(self, root: TreeNode):
        self.values = self.nodegen(root)
        self._next = next(self.values)
        
    def next(self) -> TreeNode:
        rv = self._next
        self._next = next(self.values)
        return rv

    def hasNext(self) -> bool:
        return self._next is not None

    def nodegen(self, root: TreeNode) -> [int, None]:
        next = root
        stack = []
        while next:
            while next:
                stack.append(next)
                next = next.left
            while stack:
                n = stack.pop()
                yield n.val
                if n.right:
                    next = n.right
                    break
        yield

bst = BSTIterator(maketree([7, 3, 15, None, None, 9, 20]))

print(bst.next().val)
print(bst.next().val)
print(bst.hasNext())
print(bst.next().val)
print(bst.hasNext())
print(bst.next().val)
print(bst.hasNext())
print(bst.next().val)
print(bst.hasNext())
