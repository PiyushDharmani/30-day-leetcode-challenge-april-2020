class node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.head = node(0,0)
        self.tail = node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            n = self.dict[key]
            self.remove(n)
            self.add(n)
            return n.value
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
        n = node(key,value)
        self.add(n)
        self.dict[key] = n

        if len(self.dict) > self.capacity:
            n =  self.head.next
            self.remove(n)
            del self.dict[n.key]

    def add(self, node):
        pre = self.tail.prev
        pre.next = node
        self.tail.prev = node
        node.prev = pre
        node.next = self.tail

    def remove(self, node):
        pre = node.prev
        nex = node.next
        pre.next = nex
        nex.prev = pre


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
