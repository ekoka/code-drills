# Starting from head, find item `i`.
def find(head, i): 
    j = 0
    n = head
    while n and j < i:
        n = n.next
        j += 1
    return n

def alt_find(head, i):
    n = head
    while n and i > 0:
        n = n.next
        i -= 1
    return n

def alt_find_node(head, target):
    n = head
    while n and n!=target:
        n = n.next
    return n

# Starting from node `n` move forward `count` steps.
def forward(n, count):
    while n and count > 0:
        n = n.next
        count -= 1
    return n

# Starting from head, find predecessor of item `i`.
def predecessor(head, i):
    pre = None
    n = head
    while n and i > 0:
        pre = n
        n = n.next
        i -= 1
    if n:
        return pre

# Starting from head, find and remove item `i`.
def remove(head, i):
    if i==0:
        res = head.next
        head.next = None
        return res
    pre = None
    n = head
    while n and i > 0:
        pre = n
        n = n.next
        i -= 1
    pre.next = n.next
    n.next = None
    return head

# reverse list
def reverse(head): 
    pre = None
    n = first
    while n:
        next_n = n.next
        n.next = pre
        pre = n
        n = next_n
    return pre

def reverse_sublist(head, first, last):
    after_last = last.next
    before_first = None
    n = head
    while n!=first:
        before_first = n
        n = n.next

    pre = None
    last.next = None
    n = first
    while n:
        next_n = n.next
        n.next = pre
        pre = n
        n = next_n

    if before_first:
        before_first.next = pre 
    else:
        head = pre

    first.next = after_last
    return head

# Find (higher) middle of linked list. Middle of list is first item of right half. Right half is larger than left half by one item in odd-sized list.
def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Split list in the middle. Similar to `find_middle()`, but position right before middle is also tracked for split.
def split_middle(head): 
    pre = None
    slow = head
    fast = head
    while fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next
    if not pre:
        return None, head
    pre.next = None
    return head, slow

# Find `nth` item from the end where `1st` from the end means the last item, `2nd` from the end means second to last, and so forth.
def ith_last(head, i): 
    r1 = head
    while i > 0:
        r1 += 1
        i -= 1
    r2 = head
    while r1:
        r2 = r2.next
        r1 = r1.next
    return r2

# Or alternately find the size first, since in any case the first runner must get to the end of the line.
def alt_ith_last(head, i): 
    length = 0
    n = head
    while n: length += 1
    ith_last = length - i
    n = head
    while ith_last > 0:
        n = n.next
        ith_last -= 1
    return n

# Splice segment `(first, last)` from list where `first` and `last` are inclusive indexes of respectively the first and last item of the segment to remove. 
def splice(head, first, last):
    if first is head:
        return last.next
    pre = None
    n = head
    while n != first:
        pre = n
        n = n.next
    pre.next = last.next
    return head

# swap two nodes
def swap(head, i, j):
    if i==j: return
    if i > j: i, j = j, i
    pre = None
    n = head
    k = i
    while k > 0:
        pre = n
        n = n.next
        k -= 1
    # if nodes are next to one another
    if j==i+1:
        n2 = n.next
        n.next = n2.next
        n2.next = n
        if not pre:
            head = n2
        else:
            pre.next = n2
        return head

    # find second node
    pre2 = pre
    n2 = n
    k = j - i
    while k > 0:
        pre2 = n2
        n2 = n2.next
        k -= 1
    # swap
    after_n = n.next
    n.next = n2.next
    n2.next = after_n
    pre2.next = n
    if not pre:
        # second node is now head
        head = n2
    else:
        # attach pre to second node
        pre.next = n2
    return head
