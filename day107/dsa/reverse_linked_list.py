"""
DSA Problem: Reverse Linked List
Given the head of a singly linked list, reverse the list and return its head.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

if __name__ == "__main__":
    # Example usage
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3
    head = reverse_list(n1)
    while head:
        print(head.val, end=" ")  # Output: 3 2 1
        head = head.next
