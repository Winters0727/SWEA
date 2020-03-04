import sys

sys.stdin = open('sample_input.txt')

def make_pow(man_pow, k, N):
    global used, temp, answer
    if temp <= answer:
        return None
    if N == k:
        answer = temp
    else:
        for col in range(N):
            if used[col] == 0:
                if man_pow[k][col] != 0:
                    used[col] = 1
                    temp *= man_pow[k][col]*0.01
                    make_pow(man_pow, k+1, N)
                    used[col] = 0
                    temp /= man_pow[k][col]*0.01

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    man_pow = [list(map(int, input().split())) for _ in range(N)]
    temp, answer = 1, 0
    used = [0 for _ in range(N)]
    make_pow(man_pow, 0, N)
    print('#{0} {1:.6f}'.format(tc, round(answer*100,6)))