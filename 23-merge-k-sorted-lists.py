# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        heap = []
        def addToHeap(head):
            while head != None:
                heappush(heap,head.val)
                head = head.next
        for i in lists:
            if i:
                addToHeap(i)
        if not heap:
            return None
        temp = ListNode(heappop(heap))
        head = temp
        while heap:
            temp.next = ListNode(heappop(heap))
            temp = temp.next
        return head
