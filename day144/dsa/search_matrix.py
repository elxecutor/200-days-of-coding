"""
DSA Problem: Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. Integers in each row are sorted from left to right.
"""

def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        r, c = divmod(mid, cols)
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print("Found?", search_matrix(matrix, target))  # Output: True
    target = 13
    print("Found?", search_matrix(matrix, target))  # Output: False
