"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

LC 129: Sum Root to Leaf Numbers

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.



Example 1:

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:

Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.



Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 9
    The depth of the tree will not exceed 10.

"""
from .bt import maketree

def sum_root_to_leaf_number(root):
    is_leaf = lambda n: not (n.left or n.right)
    def helper(node, S):
        if node is None:
            return 0
        if is_leaf(node):
            return 10*S + node.val
        left = helper(node.left, 10*S + node.val)
        right = helper(node.right, 10*S + node.val)
        return left + right
    return helper(root, 0)

def sum_root_to_leaf_number_iter(root):
    is_leaf = lambda n: not (n.left or n.right)
    stack = [root]
    S = [0]
    rv = 0
    while stack:
        n = stack.pop()
        s = S.pop()
        if n is None:
            continue
        res = 10*s + n.val
        if is_leaf(n):
            rv += res
            continue
        S.append(res)
        S.append(res)
        stack.append(n.right)
        stack.append(n.left)
    return rv

def sum_numbers(root):
    res = [0]
    def helper(n, s):
        if n is None: return
        s += n.val
        if not (n.left or n.right):
            res[0] += s
            return
        helper(n.left, s*10)
        helper(n.right, s*10)
    helper(root, 0)
    return res


def sum_numbers(root):
    stack = [(root, 0)]
    res = 0
    while stack:
        n, s = stack.pop()
        if not n: continue
        s += n.val
        if not any((n.left, n.right)):
            res += s
            continue
        stack.append((n.left, s*10))
        stack.append((n.right, s*10))
    return res

print(sum_root_to_leaf_number(maketree([1,2,3])))
print(sum_root_to_leaf_number(maketree([4,9,0,5,1])))
print(sum_root_to_leaf_number_iter(maketree([1,2,3])))
print(sum_root_to_leaf_number_iter(maketree([4,9,0,5,1])))
