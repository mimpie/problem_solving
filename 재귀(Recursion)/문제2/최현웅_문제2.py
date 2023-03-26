import sys

input = sys.stdin.readline

# How to solve?

# 1. 미로를 생성하고 미로의 크기와 같고 모든 원소가 빈 문자열인 2차원 배열을 하나 더 생성한다, 파이썬에서 문자열은 배열처럼 iterable 합니다.

# 2. 시작지점에서는 rignt, down 방향만 가능하다, 시작지점으로 다시 돌아오지 않기 위해 시작지점은 "0123" 으로 초기화 해줍니다.

# 3. 새로운 좌표를 방문할 수 있는 조건은 이동할 때 새로운 방향을 사용한 경우입니다. 이 조건을 만들지 않으면 u-턴을 계속해서 반복하는것과 같은 무한루프를 만날 수 밖에 없습니다.

# 4. 어떤 방향을 사용해서 새로운 좌표에 도착했을 때, 현재 좌표에서 사용할 수 없는 방향을 계산하기 위해서 나머지 연산을 사용한다 => i != (offset + 3) % 4


def movable(x: int, y: int) -> bool:
    return 0 <= x < n and 0 <= y < n and maze[x][y] != 1


def solution(x: int, y: int, offset: int) -> bool:
    if x == n - 1 and y == n - 1:
        return True

    for i, (dx, dy) in enumerate(DIRECTIONS):
        if i != (offset + 3) % 4:
            nx = x + dx
            ny = y + dy
            if movable(nx, ny) and str(i) not in visited[nx][ny]:
                visited[nx][ny] += str(i)
                if solution(nx, ny, i):
                    return True

    return False


if __name__ == "__main__":
    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    n = int(input())
    maze = [list(map(int, input().split())) for _ in range(n)]

    visited = [[""] * n for _ in range(n)]
    visited[0][0] += "0123"
    down = solution(0, 0, 2)

    visited = [[""] * n for _ in range(n)]
    visited[0][0] += "0123"
    right = solution(0, 0, 3)
    # 시작 방향이 right, down 2가지 경우중 하나라도 목표 지점에 도착할 수 있으면 Yes 를 출력 한다.
    print("Yes" if down or right else "No")
