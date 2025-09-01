"""
DSA Problem: Set Matrix Zeroes
Given a matrix, if an element is 0, set its entire row and column to 0.
"""

def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    zero_rows = set()
    zero_cols = set()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0
    return matrix

if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print("Set zeroes:", set_zeroes(matrix))  # Output: [[1,0,1],[0,0,0],[1,0,1]]
