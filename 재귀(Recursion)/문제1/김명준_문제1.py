#아이템들의 총량이 가방의 용량을 벗어나지 않으면서 가격의 합이 최대가 되는 값을 출력
how_many_item = int(input())
capacity_of_bag = int(input())
weight_of_items = list(map(int,input().split()))
pay_of_items = list(map(int,input().split()))

def find_good_choice_with_recursion(capacity,n):
    global weight_of_items
    if capacity== 0 or n == 0:
        return 0
    if weight_of_items[n-1] >capacity:
        return find_good_choice_with_recursion(capacity,n-1)
    else:
        return max(pay_of_items[n-1]+find_good_choice_with_recursion(capacity-weight_of_items[n-1],n-1),find_good_choice_with_recursion(capacity,n-1))
   
print(find_good_choice_with_recursion(capacity_of_bag,how_many_item))


# dp는 완전 탐색에서 반복 되는 연산 값을 저장하는 방식이다. 완탐으로 먼저 위 백트레킹을 통해 구현했다..
# 반복되는 계산을 먼저 찾아보자 ->  max비교와, 이전 값들에 대한 접근
# 저장공간dp의 의미를 부여하자.
# 배낭의 크기와 물건의 개수, 가격 을 비교해야하니,
# dp[i][s]는 배낭의 크기가 s일 때, i개의 물건을 넣은 가격의 최대 합으로 둔다.
# dp[i][s] = max(pay_of_items[i-1]+dp[i-1][s-weight_of_items[i-1]],dp[i-1][s])



dp = list([0 for _ in range(capacity_of_bag+1)] for i in range(how_many_item+1))
def find_good_choice_with_dp(n):
    global dp
    global pay_of_items
    for i in range(1,n+1):
        for s in range(1,capacity_of_bag+1):
            if weight_of_items[i-1]> s:
                dp[i][s] = dp[i-1][s]
            else:
                dp[i][s] = max(pay_of_items[i-1]+dp[i-1][s-weight_of_items[i-1]],dp[i-1][s])
    return dp[how_many_item][capacity_of_bag]                
print(find_good_choice_with_dp(how_many_item))