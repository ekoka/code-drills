"""
LC 002: Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    2 -> 4 -> 3
    5 -> 6 -> 4
    ------------
    7 -> 0 -> 8

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

"""
# 20
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two(n1, n2):
    carry = 0
    h3 = n3 = ListNode()
    while n1 or n2:
        if n1:
            v1 = n1.val
            v1 = v1.next
        else:
            v1 = 0
        if n2:
            v2 = n2.val 
            v2 = v2.next
        else:
            v2 = 0
        v3 = v1 + v2 + carry
        carry = 0
        if v3 >= 10:
            v3 %= 10
            carry = 1
        n3.next = ListNode(v3)
        n3 = n3.next
    if carry > 0:
        n3.next = ListNode(carry)
    return h3.next
            
# more efficient
def add_two(n1, n2):
    v1 = 0
    unit = 1
    while n1:
        v1 += n1.val * unit
        unit *= 10
        n1 = n1.next
    v2 = 0
    unit = 1
    while n2:
        v2 += n2.val * unit
        unit *= 10
        n2 = n2.next
    v3 = v1 + v2
    h3 = n3 = ListNode(0)
    while v3:
        n3.next = ListNode(0)
        n3 = n3.next
        n3.val = v3 % 10
        v3 = (v3 - n3.val)//10
    return h3.next if h3.next else h3

l1 = makelist([2,4,3])
l2 = makelist([5,6,4])
l3 = add_lists(l1, l2)
print(l3)
l3 = add_two(l1, l2)
print(l3)
# [7,0,8]


l1 = makelist([0])
l2 = makelist([0])
l3 = add_lists(l1, l2)
print(l3)
l3 = add_two(l1, l2)
print(l3)
# [0]


l1 = makelist([9,9,9,9,9,9,9])
l2 = makelist([9,9,9,9])
l3 = add_lists(l1, l2)
print(l3)
l3 = add_two(l1, l2)
print(l3)
# Output: [8,9,9,9,0,0,0,1]
