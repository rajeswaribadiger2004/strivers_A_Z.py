# Definition for singly-linked list.
class Node:
    def __init__(self, val: int):
        self.data = val
        self.next = None


class Solution:
    def searchValue(self, head: 'Node', key: int) -> bool:
        current = head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
