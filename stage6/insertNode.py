class Node:
    def __init__(self, data: int, next: 'Node' = None):
        self.data = data
        self.next = next


class Solution:
    def insertAtHead(self, head: 'Node', newData: int) -> 'Node':
        newNode = Node(newData, head)
        return newNode

    def printList(self, head: 'Node') -> None:
        temp = head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
