"""
DSA Problem: Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
            return val
        return None

    def top(self):
        return self.stack[-1] if self.stack else None

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None

if __name__ == "__main__":
    ms = MinStack()
    ms.push(3)
    ms.push(5)
    ms.push(2)
    ms.push(1)
    print("Min:", ms.get_min())  # Output: 1
    ms.pop()
    print("Min:", ms.get_min())  # Output: 2
