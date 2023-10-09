def count_diff(board, start_row, start_col, pattern):
    count = 0
    for i in range(8):
        for j in range(8):
            if board[start_row + i][start_col + j] != pattern[i][j]:
                count += 1
    return count

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

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

min_diff = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        diff1 = count_diff(board, i, j, pattern1)
        diff2 = count_diff(board, i, j, pattern2)
        min_diff = min(min_diff, diff1, diff2)

print(min_diff)