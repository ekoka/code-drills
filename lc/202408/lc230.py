"""
### LC 230: Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

     3
    / \
   1   4
    \
     2

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
           5
          / \
         3   6
        / \
       2   4
      /
     1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

15:01
"""
def find_kth(root, k):
    if not root:
        return None, k
    left, count = find_kth(root.left, k)
    if count==0:
        return left, 0
    if count==1:
        return root, 0
    return find_kth(root.right, count - 1)

def kth_smallest(root, k):
    inf = float('inf')
    res = [None]
    count = [0]
    def helper(n):
        if res[0]: return 0
        if not n: return 0
        helper(n.left)
        count[0] += 1
        if count[0]==k:
            res[0] = n
            return
        helper(n.right)
    helper(root)
    return res[0].val

# assuming node is augmented to keep track of subtree node count
class TreeNode:
    def __init__(self, val: int=0, left :'TreeNode'=None, right: 'TreeNode'=None):
        self.val = val
        self.left = left
        self.right = right
        self.count = 1

def count_subtree_nodes(root):
    def helper(node):
        if not node: return 0
        lc = helper(node.left)
        rc = helper(node.right)
        node.count = lc + rc + 1
        return node.count
    return helper(root)

def kth_smallest(root, k):
    cur_k = subtree_size(root.left) + 1
    if cur_k==k:
        return root
    if cur_k > k:
        return kth_smallest(root.left, k)
    if cur_k < k:
        return kth_smallest(root.right, k-cur_k)

def subtree_size(node):
    if not node: return 0
    return node.count

from .bt import maketree

print(find_kth(maketree([3,1,4,None,2]), 1))
print(find_kth(maketree([7,3,8,2,4,None,None,1]), 5))
