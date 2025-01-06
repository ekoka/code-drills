
"""
LC 206 : Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# 30
from ll import makelist

def reverse_ll_iter(L):
    prev = None
    nxt = L
    while nxt:
        nxt_next = nxt.next
        nxt.next = prev
        prev = nxt
        nxt = nxt_next
    return prev

def reverse_ll(L):
    def helper(prev, nxt):
        if nxt is None:
            return prev
        rv = helper(nxt, nxt.next)
        nxt.next = prev
        return rv
    return helper(None, L)


head = [1,2,3,4,5]
rv1 = reverse_ll_iter(makelist(head))
rv2 = reverse_ll(makelist(head))
print(rv1)
print(rv2)
# Output: [5,4,3,2,1]

head = [1,2]
rv1 = reverse_ll_iter(makelist(head))
rv2 = reverse_ll(makelist(head))
print(rv1)
print(rv2)
#Output: [2,1]
