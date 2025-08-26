"""
DSA Problem: Merge Two Sorted Linked Lists
Merge two sorted linked lists and return it as a new sorted list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = ListNode()
    curr = dummy
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next

if __name__ == "__main__":
    # Example usage
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(4)
    a1.next = a2
    a2.next = a3
    b1 = ListNode(1)
    b2 = ListNode(3)
    b3 = ListNode(4)
    b1.next = b2
    b2.next = b3
    head = merge_two_lists(a1, b1)
    while head:
        print(head.val, end=" ")  # Output: 1 1 2 3 4 4
        head = head.next
