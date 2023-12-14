"""
LC 021 : Merge Two Sorted Lists


Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""

# 21 - 30 (100%)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    head = ListNode()
    list3 = head
    while list1 and list2:
        if list1.val <= list2.val:
            list3.next = list1
            list1 = list1.next
        else:
            list3.next = list2
            list2 = list2.next 
        list3 = list3.next
    if not list1:
        list3.next = list2
    elif not list2:
        list3.next = list1
    return head.next
