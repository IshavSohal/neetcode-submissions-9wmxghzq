class LinkedListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.numKeys = 0
        self.lru = None
        self.mru = None
        

    def get(self, key: int) -> int:
        # print("")
        # print("get: ", key)
        # print("cache: ", self.cache)
        # print("lru: ", self.lru)
        # print("mru: ", self.mru)
        if key in self.cache: # we assume numKeys > 0, and that curr will not be none
            # Find corresponding node in LL, and make it the MRU node
            curr = self.lru
            prev = None
            while curr is not None and curr.key != key:
                prev = curr
                curr = curr.next

            # If the accessed key is already the MRU, there is nothing to rearrange
            if curr.key != self.mru.key:
                if prev is not None:
                    prev.next = curr.next

                self.mru.next = curr
                self.mru = curr
                
                if curr.next is None:
                    self.lru = curr
                elif prev is None:
                    self.lru = curr.next

                curr.next = None

            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        # print("")
        # print("put: ", key)
        # print("cache: ", self.cache)
        # print("lru: ", self.lru)
        # print("mru: ", self.mru)
        if key in self.cache:
            # Find corresponding node in LL, and make it the MRU node
            curr = self.lru
            prev = None
            while curr.key != key:
                prev = curr
                curr = curr.next

            # If the accessed key is already the MRU, there is nothing to rearrange
            if curr.key != self.mru.key:
                if prev is not None:
                    prev.next = curr.next

                self.mru.next = curr
                self.mru = curr
                
                if curr.next is None:
                    self.lru = curr
                elif prev is None:
                    self.lru = curr.next

                curr.next = None
            
        elif self.numKeys < self.capacity:
            # Add the new entry in to the LL, and make it the MRU node
            new_node = LinkedListNode(key)

            if self.numKeys == 0:
                self.lru = new_node
            else:
                self.mru.next = new_node

            self.mru = new_node

            self.numKeys += 1

        else:
            # Add the new entry
            new_node = LinkedListNode(key)
            self.mru.next = new_node
            self.mru = new_node  

            # Remove the LRU entry from the cache and the LL
            lru_key = self.lru.key
            self.lru = self.lru.next

            del self.cache[lru_key]

        # Update entry in cache
        self.cache[key] = value
        
