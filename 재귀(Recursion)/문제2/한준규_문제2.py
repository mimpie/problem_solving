# 파일 입력 생략
# 인접행렬 방식, BFS 응용 문제
# 'U턴의 의미'  -> 뒤 돌아감 + 1칸
# '바라보고 있는 방향을 신경써서' 직진, 우회전, U턴 해야함

from collections import deque

T = int(input())
for i in range(T):

    n = int(input())
    board = []
    start_straight, start_right = [0,0,0], [0,0,1] # x, y, look

    for j in range(n):
        board.append(list(map(int, input().split())))
    
    end_x, end_y = map(int, input().split())


    q = deque()
    q.append(start_straight)
    q.append(start_right)
    
    # 각 방향별로, visited 확인 해줘야하며, 모든 방향이 방문된 방향이면, 해당 노드는 방문을 했다.
    visited = [ [[False for _ in range(4)] for _ in range(n)] for _ in range(n)]

    # look = [1,2,3,4]

    # 상하좌우 경우는 다 적어두지만, look의 값에 따라 세 가지 경우만 적용
    # 이렇게 배치해야 연속 3개된 좌표가 직진, 우회전, U턴이라 편할듯

    # 방향
    dx = [0,1,0,-1] * 2
    dy = [1,0,-1,0] * 2

    while q:
        x,y,look = q.popleft()
        tmp_dx = dx[look:look+3]
        tmp_dy = dy[look:look+3]

        for new_x, new_y in zip(tmp_dx, tmp_dy):
            tmp_x = x + new_x
            tmp_y = y + new_y 
            look = dx.index(new_x)
            # print(look)
            if ( tmp_x < 0 or tmp_x >= n ) or ( tmp_y < 0 or tmp_y >= n) or ( board[tmp_x][tmp_y] ):
                continue
            if visited[tmp_x][tmp_y][look]:
                continue
            else:
                visited[tmp_x][tmp_y][look] = True
                q.append([tmp_x, tmp_y, look])
    
    # print(visited[end_x][end_y])
    if any(visited[end_x][end_y]):
        print("Yes")
    else:
        print("No")