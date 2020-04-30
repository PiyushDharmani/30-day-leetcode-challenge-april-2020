class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = collections.deque()
        self.dic = collections.defaultdict(int)
        for num in nums:
            self.add(num)


    def showFirstUnique(self) -> int:

        while len(self.queue) > 0 and self.dic[self.queue[0]] > 1:
            self.queue.popleft()
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue[0]


    def add(self, value: int) -> None:
        if value in self.dic:
            self.dic[value]+=1
        else:
            self.dic[value] = 1
            self.queue.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)



# class Node:
#     def __init__(self,key):
#         self.key = key
#         self.next  = None
#         self.prev = None

# class FirstUnique:

#     def __init__(self, nums: List[int]):
#         self.dic = dict()
#         self.head = Node(-1)
#         self.tail = Node(-1)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#         for num in nums:
#             self.add(num)


#     def showFirstUnique(self) -> int:
#         return self.head.next.key


#     def add(self, value: int) -> None:
#         if value in self.dic.keys():
#             self.remove(value)
#         else:
#             n = Node(value)
#             self.dic[value] = n
#             pre = self.tail.prev
#             pre.next = n
#             self.tail.prev = n
#             n.next = self.tail
#             n.prev = pre

#     def remove(self,value):
#         node = self.dic[value]
#         pre = node.prev
#         nex = node.next
#         pre.next = nex
#         nex.prev = pre
#         del self.dic[value]
