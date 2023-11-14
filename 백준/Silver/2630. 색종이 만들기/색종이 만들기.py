n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]


def cnt_paper_color(x, y, n):
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                top_left = cnt_paper_color(x, y, n//2)
                top_rght = cnt_paper_color(x, y+n//2, n//2)
                bot_left = cnt_paper_color(x+n//2, y, n//2)
                bot_rght = cnt_paper_color(x+n//2, y+n//2, n//2)
                return (top_left[0] + top_rght[0] + bot_left[0] + bot_rght[0], 
                        top_left[1] + top_rght[1] + bot_left[1] + bot_rght[1])
    return (1, 0) if color == 0 else (0, 1)


white, blue = cnt_paper_color(0, 0, n)
print(white)
print(blue)
