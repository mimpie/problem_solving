dx = [-1,0,1,0]
dy = [0,1,0,-1]
#direction이 0 1 2 3  방향
# 1일경우 1 혹은 2
# 2일 경우 2 혹은 3 으로 이동한다.
 
def can_i_exit(visited_tmp, now_x,now_y,direction):
    global mirror
    global flag  
    global mirror_size
    global dx,dy
    global exit_x, exit_y

    if now_x == exit_x and now_y == exit_y:
        flag = True
        return  
    else:
        #우회전
        next_right_direction = (direction + 1)%4
        next_x = now_x + dx[next_right_direction]
        next_y = now_y + dy[next_right_direction]
        if 0 <= next_x <= mirror_size-1 and 0<= next_y <= mirror_size-1 and visited_tmp[next_x][next_y]== False and mirror[next_x][next_y]!=1:
            visited_tmp[next_x][next_y] = True
            can_i_exit(visited_tmp,next_x, next_y,next_right_direction)

        #직진
        next_x = now_x + dx[direction]
        next_y = now_y + dy[direction]
        if 0 <= next_x <= mirror_size-1 and 0<= next_y <= mirror_size-1 and visited_tmp[next_x][next_y]==False and mirror[next_x][next_y]!=1:
            visited_tmp[next_x][next_y] = True
            can_i_exit(visited_tmp,next_x, next_y,direction)
       
        #유턴
        u_turn_direction = (direction + 2)%4
        next_x = now_x - dx[direction]
        next_y = now_y - dy[direction]
        if 0 <= next_x <= mirror_size-1 and 0<= next_y <= mirror_size-1 and visited_tmp[next_x][next_y]!=3  and mirror[next_x][next_y]!=1 :
            visited_tmp[next_x][next_y] = 3
            can_i_exit(visited_tmp,next_x, next_y,u_turn_direction)

   
flag = False
test_case_count = int(input())
for _ in range(test_case_count):
    flag = False
    mirror_size = int(input())
    mirror = []
    for u in range(mirror_size):
        mirror.append(list(map(int,input().split())))
    exit_x,exit_y = map(int,input().split())
    visited = list([False]*(mirror_size+1) for _ in range(mirror_size+1))
    #초기화 완료
    visited[0][0] = True
    can_i_exit(visited,0,0,1)
    #함수 실행
    if flag:
        print("yes")
    else:
        print("No")
 