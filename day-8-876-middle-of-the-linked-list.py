# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        temp = head

        while (temp != None) and (temp.next != None):
            print (temp.val,head.val)
            temp = temp.next.next
            head = head.next

        return head
