import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = []
    for i in range(N):
        farm.append(input())
    answer = 0
    mid = N//2
    for i in range(N//2,-1,-1):
        if i == N//2:
            temp_list = farm[mid]
        else:
            temp_list = farm[i][mid-i:N-(mid-i)] + farm[2*mid-i][mid-i:N-(mid-i)]
        add_list = list(map(int,temp_list))
        answer += sum(add_list)
    print(f'#{tc}',answer)