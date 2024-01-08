"""
LC 019 : Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]



Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz



Follow up: Could you do this in one pass?
"""
# 14 - 23
from ll import makelist
def remove(head, n):
    pre = None
    slo = head
    fst = head
    i = 0
    while i < n: 
        fst = fst.next
        i += 1
    while fst:
        pre = slo
        slo = slo.next
        fst = fst.next
    if pre:
        pre.next = slo.next
        return head
    return head.next


head = [1,2,3,4,5]
n = 2
print(remove(makelist(head), n))
# Output: [1,2,3,5]

head = [1]
n = 1
# Output: []

head = [1,2]
n = 1
print(remove(makelist(head), n))
# Output: [1]
