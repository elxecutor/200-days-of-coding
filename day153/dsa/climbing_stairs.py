"""
DSA Problem: Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top. Each time you can climb 1 or 2 steps. Return the number of distinct ways to reach the top.
"""

def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    n = 5
    print("Ways to climb:", climb_stairs(n))  # Output: 8
