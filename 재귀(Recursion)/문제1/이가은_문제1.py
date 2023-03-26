import copy

'''입력 input.txt 파일로 받기'''
f = open('./input.txt', 'r')
N = int(f.readline())                           # 아이템의 개수
knapsack = int(f.readline())                    # 배낭의 용량
weight = list(map(int, f.readline().split()))   # 아이템의 무게
value = list(map(int, f.readline().split()))    # 아이템의 가격
f.close()


include = [False for _ in range(N)]              # 원소 포함 여부 판단
maxW = 0                                         # 최대값 변수 선언
maxW_subset = 0                                  # 최대값인 부분집합

''' k번째 원소까지의 Value, Weight 합을 구함 '''
def getSumValueWeight(k):
    sumValue, sumWeight = 0, 0
    for i in range(k):
        if include[i]:
            sumValue += value[i]
            sumWeight += weight[i]
    return sumValue, sumWeight

'''멱집합 구하기'''
def knap(k):
    # 전역변수 사용
    global maxW
    global maxW_subset
    
    sum = getSumValueWeight(k)
    sumValue, sumWeight = sum[0], sum[1]
    # 지금까지의 무게가 배낭 제한 무게를 넘을 시
    if sumWeight > knapsack:
        return
    # 마지막 노드 확인 시
    elif (k == N):
        # 현재까지 고려한 부분집합들의 최대값 value를 초과시
        if sumValue > maxW:
            # 최대값 갱신
            maxW = sumValue
            # 추가) include 루트를 보기 위해서 : 최대값인 부분집합(깊은 복사)
            maxW_subset = copy.deepcopy(include)
        return
    else:
        # 원소 K를 포함하지 않은 경우
        include[k] = 0
        knap(k+1)
        # 원소 K를 포함한 경우
        include[k] = 1
        knap(k+1)
        return

'''main'''
knap(0)                                                 # 0번째 원소부터 부분 집합 구하기
print(maxW)                                             # 최대값 출력
print(list(map(lambda x: 1 if x else 0, maxW_subset)))  # 최대값을 도출한 부분집합 출력
