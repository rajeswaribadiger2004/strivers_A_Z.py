# Definition for singly-linked list.
class Node:
    def __init__(self, val: int):
        self.data = val
        self.next = None


class Solution:
    def deleteTail(self, head: 'Node') -> 'Node':
        # If list is empty or has only one node
        if not head or not head.next:
            return None

        # Traverse to the second last node
        curr = head
        while curr.next.next:
            curr = curr.next

        # Delete tail node
        curr.next = None
        return head
