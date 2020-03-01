import sys

sys.stdin = open('sample_input.txt')

def DFS(n, k, cost):
    global answer, DFS_sum
    if n >= k:
        if DFS_sum < answer:
            answer = DFS_sum
    else:
        DFS_sum += cost[n]
        DFS(n+1,k, cost)
        DFS_sum -= cost[n]
        DFS_sum += t_m
        DFS(n+3, k, cost)
        DFS_sum -= t_m

T = int(input())
for tc in range(1, T+1):
    d, o_m, t_m, y = map(int,input().split())
    plan = list(map(int,input().split()))
    answer = y
    min_cost = [plan[i] * d if plan[i] != 0 else 0 for i in range(12)]
    for j in range(12):
        if min_cost[j] > o_m:
            min_cost[j] = o_m
    DFS_sum = 0
    DFS(0, 12, min_cost)
    print('#{0} {1}'.format(tc,answer))