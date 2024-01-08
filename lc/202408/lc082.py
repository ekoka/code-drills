"""
LC 082 : Remove Duplicates From Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]



Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.

"""
# 32 - 53

def remove_dupes(L):
    H = L
    pre = None
    while L:
        if L.next and L.val==L.next.val:
            L = remove_all(L)
            if pre:
                pre.next = L
            else:
                H = L
        else:
            pre = L
            L = L.next
    return H

def remove_dupes(L):
    H, pre = L, None
    while L:
        if L.next and L.val==L.next.val:
            while L.next and L.val==L.next.val:
                L = L.next
            L = L.next
            if pre:
                pre.next = L
            else:
                H = L
        else:
            pre, L = L, L.next
    return H

def remove_all(L):
    while L.next and L.val==L.next.val:
        L = L.next
    return L.next
