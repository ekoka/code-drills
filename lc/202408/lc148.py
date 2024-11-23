"""
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:

Input: head = []
Output: []

Constraints:

    The number of nodes in the list is in the range [0, 5 * 104].
    -105 <= Node.val <= 105

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""
#
def count(head):
    rv = 0
    while head:
        rv += 1
        head = head.next
    return rv

def sortlist(head):
    def helper(left, count):
        if count<=1: return left
        l_cnt = count//2
        right = split(left, l_cnt)
        l = helper(left, l_cnt)
        r = helper(right, count - l_cnt)
        return merge(l, r)
    return helper(head, count(head))

def split(head, l_cnt):
    if l_cnt==0: return
    r = head
    i = 0
    pre = None
    while i < l_cnt:
        pre = r
        r = r.next
        i += 1
    pre.next = None
    return r

def merge(l, r):
    ls_head = ls = ListNode()
    while l or r:
        if not l:
            ls.next = r
            break
        elif r:
            ls.next = l
            break
        elif l.val > r.val:
            ls.next, ls = r, r
            r = r.next
        else:
            ls.next, ls = l, l
            l = l.next
    return ls_head.next

# More optimal and using a fast runner to split the array instead of a counter
def sortlist(head):
    def helper(left):
        if not left: return
        if not left.next: return left
        right = split(left)
        l = helper(left)
        r = helper(right)
        return merge(l, r)
    return helper(head)

def split(head):
    slw = fst = head
    while fst.next and fst.next.next:
        slw = slw.next
        fst = fst.next.next
    right = slw.next
    slw.next = None
    return right

def merge(l, r):
    ls_head = ls = ListNode()
    while l and r:
        if l.val > r.val:
            ls.next, ls = r, r
            r = r.next
            continue
        ls.next, ls = l, l
        l = l.next
    if not l:
        ls.next = r
    elif not r:
        ls.next = l
    return ls_head.next

### Being practical

def sortlist(head):
    n = head
    ref = {}
    vals = []
    while n:
        ref.setdefault(n.val, []).append(n)
        vals.append(n.val)
        n = n.next
    vals.sort()
    res = n = ListNode()
    for v in vals:
        n.next = ref[v].pop()
        n = n.next
    n.next = None
    return res.next

def sortlist(head):
    if not head: return
    lst = []
    ptr = head
    while ptr:
        lst.append(ptr)
        ptr = ptr.next
    sort(lst)
    pre = lst[-1]           # make last node the predecessor
    for node in lst:
       pre.next = node 
       pre = node
    lst[-1].next = None     # unlink last node
    return lst[0]



def sort(lst):
    start = 0
    stop = len(lst)
    p = lomuto_partition(lst, start, stop)
    sort(lst, start, p)
    sort(lst, p+1, stop)

def sortlist(head):
    n = head
    ref = {}
    vals = []
    while n:
        ref.setdefault(n.val, []).append(n)
        vals.append(n.val)
        n = n.next
    sort(vals)
    res = n = ListNode()
    for v in vals:
        n.next = ref[v].pop()
        n = n.next
    n.next = None
    return res.next

def lomuto_partition(lst, start, stop):
    lo = start
    hi = start
    pivot = stop - 1
    while hi < pivot:
        if lst[hi] < lst[pivot]:
            lst[hi], lst[lo] = lst[lo], lst[hi]
            lo += 1
        hi += 1
    lst[lo], lst[pivot] = lst[pivot], lst[lo]
    return lo

def hoare_partittion(lst, start, stop):
    pivot = start
    lo = start+1
    hi = stop-1
    while  lo <= hi:
        # decrement hi
        while lo < hi and lst[hi] >= lst[pivot]:
            hi -= 1
        # increment lo
        while lo < hi and lst[lo] < lst[pivot]:
            lo += 1
        if lo <= hi:
            lst[lo], lst[hi] = lst[hi], lst[lo]
    lst[hi], lst[pivot] = lst[pivot], lst[hi]
    return hi

def sort(lst):
    random.shuffle(lst)
    stack = [(0, len(lst))]
    while stack:
        start, stop = stack.pop()
        if start==stop: continue
        p = lomuto_partition(lst, start, stop)
        stack.append((start, p))
        stack.append((p+1, stop))


lst2 = list(lst)

