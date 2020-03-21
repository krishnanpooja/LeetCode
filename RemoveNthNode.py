'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        begin = head
        count = 0
        length = 1
        prev = None
        while(head.next):
            head =head.next
            length +=1
        print(length)
        delete_node = length -n
        print(delete_node)
        head = begin
        while(head and count<delete_node):
            prev = head
            head = head.next
            count += 1
        if(head):
            if(prev):
                prev.next = head.next
        del head
        return begin
