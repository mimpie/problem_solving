# DFS? => O(2^N) => 시간초과(일반적으로)
# 겹치는 계산을 메모제이션해서 계산을 줄이자 
n = int(input())
w = int(input())
w_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))

# 선택 하느냐 마느냐 기록을 통해 중복 계산 줄여야함
dp = [[0 for _ in range(w+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,w+1):
        dp[i][j] = dp[i-1][j]
        if j-w_list[i-1] >= 0:
            dp[i][j] = max(dp[i-1][j-w_list[i-1]] + v_list[i-1], dp[i-1][j])
            
print(dp[n][w])
