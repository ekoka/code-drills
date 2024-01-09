"""
LC 086 : Partition List

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]

Constraints:

    The number of nodes in the list is in the range [0, 200].
    -100 <= Node.val <= 100
    -200 <= x <= 200

"""
# 57

def partition(head, x):
    lo_head = lambda: None
    hi_head = lambda: None
    lo = lo_head
    hi = hi_head
    while head:
        if head.val < x:
            lo.next = head
            lo = head
        else:
            hi.next = head
            hi = head
        head = head.next
    hi.next = None
    lo.next = hi_head.next
    return lo_head.next

def partition(head, x):
    before = b = ListNode()
    after = a = ListNode()
    n = head
    while n:
        if n.val >= x:
            a.next = n
            a = a.next
        else:
            b.next = n
            b = b.next
        nxt_n = n.next
        n.next = None # not necessary
        n = nxt_n
    b.next = after.next
    return before.next

from ll import makelist
head = makelist([1,4,3,2,5,2])
x = 3
print(partition(head, x))
# Output: [1,2,2,4,3,5]

head = makelist([2,1])
x = 2
print(partition(head, x))
# Output: [1,2]
