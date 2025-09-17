"""
DSA Problem: Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
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
