"""
LC 146: LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:

    1 <= capacity <= 3000
    0 <= key <= 104
    0 <= value <= 105
    At most 2 * 105 calls will be made to get and put.

"""
# 25

class LRUCache: # using a linked list 

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {} # key: (predecessor, node)
        self._lru_head = None
        self._lru = None

    def get(self, key: int) -> int:
        if key not in self.nodes: return -1
        pre, n = self.nodes[key]
        self._lru_update(pre, n)
        return n.val[1]

    def put(self, key: int, value: int):
        if key in self.nodes:
            pre, n = self.nodes[key]
            n.val = (key, value) # update
            self._lru_update(pre, n)
        else:
            if len(self.nodes)==self.capacity:
                self._lru_pop()
            n = Node((key, value))
            self._lru_push(n)

    def _lru_update(self, pre, n):
        if pre is None: return False # nothing to change
        pre.next = n.next
        if pre.next:
            self.nodes[pre.next.val[0]] = (pre, pre.next)
        else:
            self._lru = pre
        self._lru_push(n)

    def _lru_pop(self):
        pre_lru, lru = self.nodes.pop(self._lru.val[0])
        if pre_lru:
            pre_lru.next = None
            self._lru = pre_lru
        else:
            self._lru = None
            self._lru_head = None

    def _lru_push(self, n): 
        if self._lru_head:
            self.nodes[self._lru_head.val[0]] = (n, self._lru_head)
        n.next = self._lru_head 
        self._lru_head = n
        self.nodes[n.val[0]] = (None, n)
        if self._lru is None:
            self._lru = n


import collections
class LRUCache: # using OrderedDict
    
    def __init__(self, capacity):
        self.items = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.items: return -1
        item = self.items[key]
        self.items.move_to_last(key)
        return item

    def put(self, key, value):
        if key in self.items:
            self.items.move_to_last(key)
        else:
            if self.capacity==len(self.lru):
                self.items.popitem(last=False)
        self.items[key] = value


class LRUCache: # taking advantage of dict ordering (since Python 3.7)

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = {}

    def get(self, key):
        if key not in self.items: return -1
        self.items.pop(key)
        self.items[key] = val
        return val

    def put(self, key, val):
        val = self.items.pop(key, -1)
        self.items[key] = val
        if len(self.items) > self.capacity:
            k = next(iter(self.items))
            self.items.remove(k)
