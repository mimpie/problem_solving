f = open('input.txt', 'r')  # input.txt 읽어오기
T = int(f.readline())  # 테스트 케이스의 개수 입력받기 (T)

offset = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 상:0, 우:1, 하: 2, 좌:3

# T번 반복
for i in range(T):
    # 미로의 크기 입력받기 (N)
    N = int(f.readline())

    # 진입 방향 direction 기록하는 배열 (상우하좌)
    visited = [[[0,0,0,0] for i in range(N)] for i in range(N)]
    maze = []
    # (0, 0)에 있을 때, -> 방향으로 가는 게 직진이므로 우를 의미하는 1을 기본 값으로 설정
    direction = 1
    
    # 미로의 상태 입력받기 (maze)
    for j in range(N):
        maze.append(list(map(int, f.readline().split())))

    # 출구 좌표 입력받기
    end = list(map(int, f.readline().split()))
    '''좌표가 미로 범위 내에 존재하는지 판별'''
    def isOutside(cur):
        return cur[0]<0 or cur[1]<0 or cur[0]>=N or cur[1]>=N

    '''애국이 순환함수'''
    def navigate(cur, direction):
        if isOutside(cur): # 현좌표가 미로 범위를 벗어난 경우
            return False
        
        elif cur == end: # 현좌표가 출구좌표인 경우
            return True
        
        # direction 방향으로 지나갔음을 표시
        visited[cur[0]][cur[1]][direction] = 1
        
        # 직진(0), 우회전(1), 유턴(2) 체크
        for k in range(3):
            pos = cur.copy()
            new_direction = (direction+k)%4
            pos[0] += offset[new_direction][0]
            pos[1] += offset[new_direction][1]

            # 미로 범위 내 && 온 방향 아님 && 벽이 아님
            if not isOutside(pos) and visited[pos[0]][pos[1]][new_direction] == 0 and maze[pos[0]][pos[1]] == 0:
               if navigate(pos, new_direction):
                    return True
                
        return False
            
    if navigate([0, 0], direction):
        print('Yes')
    else:
        print('No')

f.close()
