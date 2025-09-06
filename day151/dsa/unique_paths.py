"""
DSA Problem: Unique Paths
A robot is located at the top-left corner of an m x n grid. The robot can only move either down or right at any point in time. Find the number of possible unique paths to the bottom-right corner.
"""

def unique_paths(m, n):
    dp = [[1]*n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

if __name__ == "__main__":
    m, n = 3, 7
    print("Unique paths:", unique_paths(m, n))  # Output: 28
