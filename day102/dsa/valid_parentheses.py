"""
DSA Problem: Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
"""

def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

if __name__ == "__main__":
    s = "()[]{}"
    print("Is valid?", is_valid(s))  # Output: True
    s = "([)]"
    print("Is valid?", is_valid(s))  # Output: False
