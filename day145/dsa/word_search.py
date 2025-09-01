"""
DSA Problem: Word Search
Given a 2D board and a word, find if the word exists in the grid.
"""

def exist(board, word):
    rows, cols = len(board), len(board[0])
    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
            return False
        temp = board[r][c]
        board[r][c] = '#'
        found = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
        board[r][c] = temp
        return found
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False

if __name__ == "__main__":
    board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    word = "ABCCED"
    print("Exists?", exist(board, word))  # Output: True
    word = "SEE"
    print("Exists?", exist(board, word))  # Output: True
    word = "ABCB"
    print("Exists?", exist(board, word))  # Output: False
