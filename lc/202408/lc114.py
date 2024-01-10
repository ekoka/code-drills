"""
Given the root of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.

        1                    1
       / \                    \
      2   5        =>          2
     / \   \                    \
    3   4   6                    3
                                  \
                                   4
                                    \
                                     5
                                      \
                                       6

Example 1:

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [0]
Output: [0]

Constraints:

The number of nodes in the tree is in the range [0, 2000].

    -100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?

Input: root = [1,2,5,3,4,null,6]

    1
   / \
  2   5
 / \   \
3   4   6
"""


class Node:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.left = l
        self.right = r

    def __str__(self):
        return f'{self.val}' if is_leaf(self) else f'{self.val}, {self.left}, {self.right}'

def flatten(root):
    n = root
    while n:
        if not n.left: 
            n = n.right
        else:
            pre = iot_predecessor(n)
            pre.right = n
            nxt_n = n.left 
            n.left = None
            n = nxt_n
    return root

def iot_predecessor(node):
    pre = node.left
    while pre.right:
        pre = pre.right
    return pre

N = Node
root = N(1, l=N(2, l=N(3), r=N(4)), r=N(5, l=None, r=N(6)))
L = preot_flatten(root)
print(f'{root}')
