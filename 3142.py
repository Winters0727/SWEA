import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    single, twin = M, 0
    while True:
        if (single+twin*2) == N:
            break
        single -= 1
        twin += 1
    print(f'#{tc}',single,twin)