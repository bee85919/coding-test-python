def solution(game_board, table):
    n = len(game_board)
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]

    # BFS를 이용해 mat에서 num 값(블록 또는 빈 공간)을 찾아 그룹화된 도형의 리스트로 반환하는 함수
    def bfs(mat, num):
        # 방문 여부를 저장하는 2차원 리스트
        visit = [[0]*n for _ in range(n)]
        # 발견된 도형들을 저장할 리스트
        shapes = []

        # mat 전체를 순회
        for i in range(n):
            for j in range(n):
                # 현재 위치가 이미 방문한 곳이거나 찾고자 하는 num 값이 아닌 경우 continue를 이용해 스킵
                if mat[i][j] != num or visit[i][j]:
                    continue

                # 현재 위치에서 시작하는 새로운 도형을 저장할 리스트
                shape = []
                # BFS를 위한 큐. 현재 위치를 시작으로 함.
                queue = [[i, j]]
                # 현재 위치는 방문했음을 표시
                visit[i][j] = 1
                
                # BFS 실행
                while queue:
                    r, c = queue.pop(0)   # 현재 방문하고 있는 위치
                    shape.append([r, c])  # 도형에 현재 위치 추가
                    for d in range(4):    # 현재 위치의 상하좌우 검사
                        nr, nc = r + dr[d], c + dc[d]
                        # 새로운 위치가 경계 안에 있고, 아직 방문하지 않았으며, 찾고자하는 num 값인 경우
                        if 0 <= nr < n and 0 <= nc < n and not visit[nr][nc] and mat[nr][nc] == num:
                            queue.append([nr, nc])  # 큐에 추가
                            visit[nr][nc] = 1       # 방문 표시
                            
                # 현재까지 찾은 도형을 shapes 리스트에 추가
                shapes.append(shape)
        
        # 발견된 도형들의 리스트 반환
        return shapes

    # 도형의 좌표를 정규화하고 문자열로 변환하는 함수
    def hashing(shape):
        min_r, min_c = min([s[0] for s in shape]), min([s[1] for s in shape])
        normalized = [[s[0]-min_r, s[1]-min_c] for s in shape]
        normalized.sort()
        return ''.join(str(s) for sub in normalized for s in sub)

    # 도형의 좌표를 90도 회전시키는 함수
    def rotate(shape):
        return [[s[1], -s[0]] for s in shape]

    # table에서 블록들을 찾고, game_board에서 빈칸들을 찾는다
    blocks = bfs(table, 1)
    blanks = bfs(game_board, 0)

    # 블록들의 해시값을 계산하고 이를 딕셔너리에 저장
    block_hashes = {}
    for block in blocks:
        block_hash = hashing(block)
        block_hashes[block_hash] = block_hashes.get(block_hash, 0) + 1

    answer = 0  # 매칭된 블록의 총 크기를 저장할 변수

    # game_board의 각 빈칸에 대해서 매칭되는 블록을 table에서 찾는다
    for blank in blanks:
        # 해당 빈칸이 이미 다른 블록과 매칭되었는지 확인하는 플래그
        matched = False

        # 빈칸을 4번 90도씩 회전시키면서 해당 빈칸에 매칭되는 블록이 있는지 검사
        for _ in range(4):
            # 만약 해당 빈칸이 이미 다른 블록과 매칭되었다면 더 이상의 회전 및 검사는 필요 없으므로 반복문 종료
            if matched:
                break

            # 현재 빈칸의 해시 값을 계산
            blank_hash = hashing(blank)

            # 해당 해시 값과 일치하는 블록이 block_hashes 딕셔너리에 존재하는지 확인
            if block_hashes.get(blank_hash):
                # 매칭된 블록의 개수를 1 감소시킴
                block_hashes[blank_hash] -= 1
                
                # 해당 블록의 크기만큼 answer에 더함 (해당 블록이 game_board에 채워짐을 의미)
                answer += len(blank)

                # 해당 빈칸이 매칭되었음을 표시
                matched = True

            # 빈칸을 90도 회전
            blank = rotate(blank)

    return answer