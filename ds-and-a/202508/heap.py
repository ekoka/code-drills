def push(heap, value):
    heap.append(value)
    sift_up(heap)

def pop(heap):
    last = len(heap) - 1
    array_swap(heap, 0, last)
    value = heap.pop()
    sift_down(heap, 0, last)
    return value

def heapify(array):
    # start the heapify process at the middle
    size = len(array)
    parent = size//2 
    while -1 < parent:
        sift_down(array, parent, size)
        parent -= 1

def sort(heap):
    index = len(heap)-1
    while 0 < index:
        popstore(heap, index)
        index -= 1

def popstore(heap, index):
    array_swap(heap, 0, index)
    sift_down(heap, 0, index)

def build(array):
    heap = []
    for v in array:
        push(heap, v)
    return heap

def pushpop(heap, value):
    if value >= heap[0]: return value
    res = heap[0]
    heap[0] = value
    sift_down(heap, 0, len(heap))
    return res

# -- utils

def sift_down(heap, parent, stop):
    child = maxchild(heap, parent, stop)
    while -1 < child and heap[parent] < heap[child]:
        array_swap(heap, parent, child)
        parent = child
        child = maxchild(heap, parent, stop)

def maxchild(heap, parent, stop):
    left = (parent*2) + 1
    if stop <= left: return -1
    right = left + 1
    if stop <= right: return left
    return right if heap[left] < heap[right] else left

def array_swap(heap, i, j): 
    heap[i], heap[j] = heap[j], heap[i]

def sift_up(heap):
    child = len(heap)-1
    parent = (child-1)//2
    while 0 < child and heap[parent] < heap[child]: 
        array_swap(heap, parent, child)
        child = parent
        parent = (child-1)//2

if __name__=="__main__":
    a = lambda: [3, 8, 2, 38, 83, 24, 8, 6, 72]

    # testing heapify, sort
    t = a()
    heapify(t)
    sort(t)
    print(t)
    assert t==sorted(a())

    # testing build, push
    t = build(a())
    sort(t)
    print(t)
    assert t==sorted(a())

    # testing pop
    t = a()
    heapify(t)
    acc = []
    while t:
        try:
            acc.append(pop(t))
        except IndexError:
            break
    print(acc)
    assert acc==sorted(a(), reverse=True)
