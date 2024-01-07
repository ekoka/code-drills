"""
LC 138 : Copy List With Random Pointers

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

Example 1:

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:

    0 <= n <= 1000
    -104 <= Node.val <= 104
    Node.random is null or is pointing to some node in the linked list.

"""
# 32

def copy(head):
    if not head: return
    n = head
    # duplicating
    while n:
        cpy = Node(n.val, n.next, n.random)
        n.next = cpy
        n = cpy.next
    n = head
    # resolving random
    while n:
        cpy = n.next
        if cpy.random:
            cpy.random = cpy.random.next
        n = cpy.next
    # unzipping copy and original
    n = head
    rv = n.next
    while n:
        cpy = n.next
        n.next = cpy.next
        if cpy.next:
            cpy.next = cpy.next.next
        n = n.next
    return rv

def copy(head):
    if not head: return 
    n = head
    # dupicate list 
    while n:
        cpy = Node(n.val,n.next,n.random)
        n.next = cpy
        n = cpy.next
    n = head
    # link to random copy
    while n:
        cpy = n.next
        n = cpy.next
        if cpy.random:
            cpy.random = cpy.random.next
    n = head
    rv = cpy = n.next
    # decouple list copy
    while cpy.next:
        n.next = cpy.next
        n = n.next
        cpy.next = cpy.next.next
        cpy = cpy.next
    # decouple last item
    n.next = None
    return rv

"""
Insight:
- Sometimes in linked list problems, you must temporarily (but subtly) modify the original linked list.
- If you need nodes in a list to point to more information than simply the next node, that supplemental information can be made into new nodes that are inserted between the original nodes then extracted later.
"""
