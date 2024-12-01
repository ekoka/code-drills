# 41 - 53 - 18
def mergeklists(lists):
    if not lists: return
    head = ListNode()
    l1 = lists.pop()
    while lists:
        l2 = lists.pop()
        merge(l1,l2, head)
        l1 = head.next
        head.next = None
    return l1

def merge(l1, l2, ptr):
    while l1 and l2:
        if l1.val > l2.val:
            ptr.next = l2
            l2 = l2.next          
        else:
            ptr.next = l1
            l1 = l1.next
        ptr = ptr.next
    if l1:
        ptr.next = l1
    else:
        ptr.next = l2

"""
Note that it doesn't matter if one of the two merged lists only has one item. 
If that item is larger than all the items of the other list, the appending operation
to the pointer will be repeated as many times that other list has elements.
Because of this repeated cost, the next divide-and-conquer approaches are more efficient.
"""

def mergeklists(lists):
    if not lists: return
    lists = collections.deque(lists)
    head = ListNode()
    while len(lists)>1:
        l1 = lists.popleft()
        l2 = lists.popleft()
        lists.append(merge(l1, l2, head))
    return lists[0]

def mergeklists(lists):
    if not lists: return
    head = ListNode()
    while len(lists)>1:
        nxt_lists = []
        while len(lists)>1:
            l1 = lists.pop()
            l2 = lists.pop()
            nxt_lists.append(merge(l1, l2, head))
        nxt_lists.extend(lists)
        lists = nxt_lists
    return lists[0]

def merge(l1, l2, head):
    ptr = head
    while l1 and l2:
        if l1.val > l2.val:
            ptr.next = l2
            l2 = l2.next          
        else:
            ptr.next = l1
            l1 = l1.next
        ptr = ptr.next
    if l1:
        ptr.next = l1
    else:
        ptr.next = l2
    return head.next
