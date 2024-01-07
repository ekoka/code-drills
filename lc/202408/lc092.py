"""
LC 092 : Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]



Constraints:

    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n


Follow up: Could you do it in one pass?
"""
# 24 - 49

# 57
def reverse_ll(head, left, right):
    # find
    i = 1
    p1 = None
    l1 = head
    while i < left:
        p1 = l1
        l1 = l1.next
        i += 1

    # reverse 
    p2 = None
    l2 = l1 
    while i <= right:
        nxt_l2 = l2.next
        l2.next = p2
        p2 = l2
        l2 = nxt_l2
        i += 1
    # p2 is head of sublist
    # l2 is first position after

    l1.next = l2
    if p1:
        p1.next = p2
        return head
    return p2
    
