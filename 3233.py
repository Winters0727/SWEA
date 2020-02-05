import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = map(int,input().split())
    answer = 0
    for i in range(0,int(A/B)):
        answer += (1+2*i)
    print(f'#{tc}',answer)