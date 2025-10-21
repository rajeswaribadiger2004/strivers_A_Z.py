# Definition for singly-linked list.
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class Solution:
    def lengthOfLinkedList(self, head: 'Node') -> int:
        count = 0
        temp = head
        
        while temp:
            count += 1
            temp = temp.next
        
        return count
