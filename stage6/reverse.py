# Definition for singly-linked list.
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    def reverseLinkedList(self, head):
        prev = None
        temp = head

        # Using 3-pointer approach
        while temp is not None:
            front = temp.next   # store next node
            temp.next = prev    # reverse the link
            prev = temp         # move prev forward
            temp = front        # move temp forward

        # new head of reversed list
        return prev


# Utility function to print the linked list
def printLinkedList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()



if __name__ == "__main__":
    # Create linked list: 1 -> 3 -> 2 -> 4
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(2)
    head.next.next.next = Node(4)

    print("Original Linked List:", end=" ")
    printLinkedList(head)

    # Reverse using Solution class
    sol = Solution()
    head = sol.reverseLinkedList(head)

    print("Reversed Linked List:", end=" ")
    printLinkedList(head)
