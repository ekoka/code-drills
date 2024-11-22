# 19
import heapq
def smallest_pairs(nums1, nums2, k):
    heap = []
    def heappush(i):
        heapq.heappush(heap, (-i[0], i[1], i[2]))
    def heappop():
        i = heapq.heappop(heap)
        return (-i[0], i[1], i[2])
    def heappeek():
        i = heap[0]
        return (-i[0], i[1], i[2])

    for i in range(len(nums1)):
        next_pair_sum = None if i==len(nums1)-1 else (nums1[i+1]+nums2[0])
        for j in range(len(nums2)):
            pair_sum = nums1[i]+nums2[j]
            heappush((pair_sum, i, j))
            if len(heap)>k:
                top = heappop()
                if pair_sum >= top[0]:
                    break
        if len(heap)==k and next_pair_sum is not None:
            if next_pair_sum >= heappeek()[0]:
                break
    res = []
    while heap:
        p = heappop()
        res.append((nums1[p[1]], nums2[p[2]]))
    return res

def smallest_pairs(nums1, nums2, k):
    heap = []
    res = []
    hpush = lambda i: heapq.heappush(heap, i)
    hpop = lambda: heapq.heappop(heap)
    # fill up heap with pairs of up to k items in
    # first array + first item in second array.
    for i in range(min(k, len(nums1))):
        hpush((nums1[i]+nums2[0], i, 0))
    # record each pair at the top of the heap,
    # then add its immediate successor as (i, j+1).
    while len(res) < k:
        key, i, j = hpop()
        res.append((nums1[i],nums2[j]))
        if j < len(nums2)-1:
            hpush((nums1[i]+nums2[j+1], i, j+1))
    return res

def smallest_pairs(nums1, nums2, k):
    # slight theoretical improvement: j now also goes up to (but does not include) k.
    heap = []
    res = []
    hpush = lambda i: heapq.heappush(heap, i)
    hpop = lambda: heapq.heappop(heap)
    for i in range(min(k, len(nums1))):
        hpush((nums1[i]+nums2[0], i, 0))
    max_j = min(k, len(nums2)) - 1
    while len(res) < k:
        key, i, j = hpop()
        res.append((nums1[i],nums2[j]))
        if j < max_j:
            hpush((nums1[i]+nums2[j+1], i, j+1))
    return res

# using heapify for better performance
def smallest_pairs(nums1, nums2, k):
    h = []
    res = []
    m = len(nums2)-1
    h = [((nums1[i]+nums2[0]), 0, (nums1[i], nums2[0])) for i in range(min(k, len(nums1)))] 
    heapq.heapify(h)
    for _ in range(k): 
        _, j, p   = heapq.heappop(h)
        res.append(p)
        if j < m: # add next
            j += 1
            heapq.heappush(h, (p[0]+nums2[j], j, (p[0], nums2[j])))
    return res

nums1 = [1,7,11]; nums2 = [2,4,6]; k = 3
print(smallest_pairs(nums1, nums2, k))
# Output: [[1,2],[1,4],[1,6]]

nums1 = [1,1,2]; nums2 = [1,2,3]; k = 2
print(smallest_pairs(nums1, nums2, k))
# Output: [[1,1],[1,1]]

nums1 = [-13,22,35,56,76]; nums2 = [-13,22,44,117,990,1000,1543,2015]; k = 25
print(smallest_pairs(nums1, nums2, k))
# Output: [[-13,-13],[-13,22],[22,-13],[35,-13],[-13,44],[56,-13],[22,22],[35,22],[76,-13],[22,44],[56,22],[35,44],[76,22],[56,44],[-13,117],[76,44],[22,117],[35,117],[56,117],[76,117],[-13,990],[-13,1000],[22,990],[22,1000],[35,990]]
