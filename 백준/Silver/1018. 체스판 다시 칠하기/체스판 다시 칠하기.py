import sys
input = sys.stdin.readline


pattern1 = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]


pattern2 = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]


def cnt_dif(board, row, col, pattern):
    count = 0
    for i in range(8):
        for j in range(8):
            if board[row + i][col + j] != pattern[i][j]:
                count += 1
    return count


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]


min_dif = float('inf')
for i in range(n-7):
    for j in range(m-7):
        min_dif = min(min_dif, cnt_dif(board, i, j, pattern1), cnt_dif(board, i, j, pattern2))


print(min_dif)