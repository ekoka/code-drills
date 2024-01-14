"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

Construct binary tree from preorder and inorder traversal.

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Also see Daily Coding Problem # 48:
https://www.dailycodingproblem.com/solution/48?token=cebcde48d24e41f8978dbc98d3e34fb0a4eea1c077879a91eb30ef83285ab95adbf48e2c

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
---------------------------------
## Solution

Recall the definitions of preorder and inorder traversals:

For preorder:

- Evaluate root node
- Evaluate left node recursively
- Evaluate right node recursively

For inorder:

- Evaluate left node recursively
- Evaluate root node
- Evaluate right node recursively

It's helpful to go over an example. Consider the following tree:

        a
       / \
      b   c
     / \ / \
    d  e f  g

The preorder traversal for this tree would be [a, b, d, e, c, f, g].

The inorder traversal for this tree would be [d, b, e, a, f, c, g].

Notice that because we always evaluate the root node first in a preorder traversal, the first element in the preorder traversal will always be the root. The second element is then either the root of the left node if there is one, or the root of the right node. But how do we know?

We can look at the inorder traversal.

Because we first traverse the left subtree in an inorder traversal, all the elements up until the root will be part of its left subtree. All elements after the root will be its right subtree.

    Preorder:
    [ a , b, d, e , c, f, g ]
    | r | left    | right   |

    Inorder:
    [ d, b, e , a , f, c, g ]
    | left    | r | right   |

    (r = root)

This gives us an idea for how to solve the problem:

- Find the root by looking at the first element in the preorder traversal
- Find out how many elements are in the left subtree and right subtree by searching for the index of the root in the inorder traversal
- Recursively reconstruct the left subtree and right subtree

The code for this problem would look like this:

    >>> def reconstruct(preorder, inorder):
    ...     if not preorder and not inorder:
    ...         return None
    ...     if len(preorder) == len(inorder) == 1:
    ...         return preorder[0]
    ...     root = preorder[0]
    ...     root_i = inorder.index(root)
    ...     root.left = reconstruct(preorder[1:1 + root_i], inorder[0:root_i])
    ...     root.right = reconstruct(preorder[1 + root_i:], inorder[root_i + 1:])
    ...     return root
"""
class TreeNode:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.left = l
        self.right = r

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


def buildtree(preorder, inorder):
    iot_index_finder = {v:i for i,v in enumerate(inorder)}
    def helper(preot, inot):
        if not preot: return
        # preot always starts with root
        n = Node(preot[0])
        iot_root = iot_index_finder[n.val]
        if iot_root==0: # no left subtree (thus child)
            # symbolic
            # n.left = helper(preot[1:1], inot[1:])
            n.right = helper(preot[1:], inot[1:])
        else:           # i is index of root and also size of left subtree
            n.left = helper(preot[1:i+1], inot[:i])
            n.right = helper(preot[i+1:], inot[i+1:])
    return helper(preorder, inorder)

# using an iterator
def buildtree(preorder, inorder):
    iot_index_finder = {v:i for i,v in enumerate(inorder)}
    preorder_iterator = iter(preorder)
    stop = len(inorder)
    def helper(iot_index):
        if iot_index==stop:
            return
        root_value = next(preorder_iterator)
        iot_root_index = iot_index_finder[root_value]
        root = Node(root_value)
        root.left = helper()
        root.right = helper()
        return root
    return helper(0, stop - 1)

# explicit explanation
def build(preorder, inorder):
    N = len(preorder)
    io_val_to_idx = {inorder[i]:i for i in range(len(inorder))}
    def bld(pr_root, io_start, io_stop):
        if pr_root>=N or io_start>=io_stop: return
        io_root = io_val_to_idx[preorder[pr_root]]
        node = TreeNode(preorder[pr_root])
        # if io subtree starts at first io item, there's no left child.
        if io_root==io_start:
            node.left = None
            node.right = bld(pr_root+1, io_start+1, io_stop)
        else:
            # if subtree starts elsewhere, then there's a left subtree, which
            # is the next item in the preorder traversal.
            # the inorder left subtree stops at the root.
            node.left = bld(pr_root+1, io_start, io_root)
            # the size of the left subtree can be used to find the right root
            # in the preorder traversal.
            size_of_left_subtree = io_root - io_start
            right_root = pr_root + size_of_left_subtree + 1
            # io subtree starts one item after io root.
            node.right = bld(right_root, io_root+1, io_sp)
        return node
    return bld(0,0,N)

# iterative, post-order traversal
def build(preorder, inorder):
    N = len(preorder)
    stack = [(0,0,N,False)]
    indexes = {v:i for i, v in enumerate(inorder)}
    res = []
    while stack:
        pr1, io1, io2, discovered = stack.pop()
        if io1>=io2: 
            res.append(None)
            continue
        if discovered:
            n = TreeNode(preorder[pr1])
            n.left = res.pop()
            n.right = res.pop()
            res.append(n)
        else:
            stack.append((pr1, io1, io2, True))
            # preot always starts with root
            io_root = indexes[preorder[pr1]]
            if io_root==io1: # no left subtree (thus child)
                stack.append((pr1+1, io1+1, io1+1, False)) # left
                stack.append((pr1+1, io1+1, io2, False)) # right
            else: 
                sz = io_root - io1
                stack.append((pr1+1, io1, io_root, False)) # left
                stack.append((pr1+1+sz, io_root+1, io2, False)) # right
    return res[0]

# iterative, pre-order traversal with accumulator (pass the parent node down)
def build(preorder, inorder):
    preroot = TreeNode()
    N = len(preorder)
    stack = [(0,0,N, preroot, False)]
    indexes = {v:i for i, v in enumerate(inorder)}
    while stack:
        pr1, io1, io2, parent, left = stack.pop()
        if io1 >= io2: continue
        n = TreeNode(preorder[pr1])
        if left:
            parent.left = n
        else:
            parent.right = n
        io_root = indexes[n.val]
        if io_root==io1: # no left subtree (thus child)
            stack.append((pr1+1, io1+1, io2, n, False)) # right
        else: 
            sz = io_root - io1
            stack.append((pr1+1, io1, io_root, n, True)) # left
            stack.append((pr1+1+sz, io_root+1, io2, n, False)) # right
    return preroot.right

# -- Test

def preot(root, acc=None):
    if acc is None:
        acc = []
    if not root:
        acc.append(None)
        return acc
    acc.append(root.val)
    preot(root.left, acc)
    preot(root.right, acc)
    return acc

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
preorder = [3,2,1,4]
inorder = [1,2,3,4]
root = build(preorder, inorder)
print(preot(root))
