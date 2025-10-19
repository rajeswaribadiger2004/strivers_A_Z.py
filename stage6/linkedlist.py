class Node:
    def __init__(self, data: int, next: 'Node' = None):
        self.data = data
        self.next = next
# Example usage (not needed on LeetCode)
arr = [2, 5, 8, 7]
head = Node(arr[0])
print(head.data)   # Output: 2
# Create a node
n1 = Node(10)
print(n1.data)   # Output: 10
print(n1.next)   # Output: None

# Link two nodes
n2 = Node(20)
n1.next = n2

print(n1.next.data)  # Output: 20
