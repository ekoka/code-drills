"""
LC 141 : Linked List Cycle
"""
# 30 - 35
def has_cycle(head):
    slo = head
    fst = head
    while fst.next and fst.next.next:
        slo = slo.next
        fst = fst.next.next
        if slo is fst:
            return True
    return False

 def has_cycle(head):
    if not head: return False
    slo = head
    fst = head.next
    while fst and fst.next:
        if slo==fst:
            return True
        slo = slo.next
        fst = fst.next.next
    return False   
