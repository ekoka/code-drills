"""
LC 61 : Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]



Constraints:

    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 109

"""
# 06
def rotate(head, k):
    if not head: return
    sz = 0
    n = head
    while n:
        sz += 1
        n = n.next
    k %= sz
    if k==0: return head   
    n1 = head
    n2 = head
    while k:
        n1 = n1.next
        k -= 1
    pre1 = None
    pre2 = None
    while n1:
        pre1 = n1
        pre2 = n2
        n1 = n1.next
        n2 = n2.next
    pre2.next = None
    pre1.next = head
    return n2

from ll import makelist
l = makelist([1])
k = 99
print(rotate(l, k))

l = makelist([1,2,3,4,5])
k = 2
print(rotate(l, k))

l = makelist([0,1,2])
k = 4
print(rotate(l, k))
