"""
DSA Problem: Rotate Image
Given an n x n 2D matrix, rotate the image by 90 degrees (clockwise).
"""

def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print("Rotated image:", rotate(matrix))  # Output: [[7,4,1],[8,5,2],[9,6,3]]
