import sys

input = sys.stdin.readline

# How to solve?
# 선택된 아이템 리스트 배열도 같이 출력해봤습니다

# 1. 가방이 최대 담을 수 있는 무게가 될때까지 순서대로 물건을 담으며 다음 함수를 호출합니다

# 함수가 종료되는 조건
# a. index > n : 더이상 담을 수 있는 아이템이 없는 경우
# b. weight >= n : 제한된 무게 이상으로 물건을 담은 경우

# 2. 함수가 종료되는 조건까지 오면 정답으로 출력할 answer 변수를 비교한 후, 최댓값으로 업데이트 해줍니다.


def solution(index: int, weight: int, money: int, num: int) -> None:
    global answer, answer_list
    if index >= n or weight >= w:
        tmp = answer
        if weight > w:
            answer = max(answer, money - num)
        else:
            answer = max(answer, money)
        # tmp != answer 즉, answer 값이 업데이트 된 경우에만 answer_list 배열을 update 해준다.
        if tmp != answer:
            answer_list = visited.copy()
        return

    for i in range(index, n):
        if not visited[i]:
            visited[i] = 1
            solution(
                index + 1, weight + weight_list[i], money + money_list[i], money_list[i]
            )
            visited[i] = 0


if __name__ == "__main__":
    n, w = int(input()), int(input())
    weight_list = list(map(int, input().split()))
    money_list = list(map(int, input().split()))
    visited = [0] * n
    answer, answer_list = 0, []

    solution(0, 0, 0, 0)
    print(answer)
    print(answer_list)
