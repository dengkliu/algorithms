# https://leetcode.com/problems/lru-cache/

# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

class Node:
    def __init__(self, key = None, value = None):
        # why do we use double linked list?
        self.prev = None
        self.next = None
        # why do we need to cache key into each node?
        self.key = key
        self.value = value

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = Node() # dummy head
        self.tail = Node() # dummy tail
        self.head.next = self.tail
        self.tail.pre = self.head
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        value = node.value

        self._move_to_front(node)

        return value

    #. head->3->1->2->4
    #. head<-3<-1<-2<-4
    def _move_to_front(self, node):
        # Firt remove this node
        node.next.prev = node.prev
        node.prev.next = node.next
        # then add it to front
        self._add_to_front(node)
    
    def _add_to_front(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    # head->1->tail
    # head<-1<-tail
    def _evict_tail(self):
        node_to_evict = self.tail.prev
        prev = node_to_evict.prev
        prev.next = self.tail
        self.tail.prev = prev
        node_to_evict.next = None
        node_to_evict.prev = None
        del self.cache[node_to_evict.key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_front(node)
            if len(self.cache.keys()) > self.capacity:
                self._evict_tail()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)