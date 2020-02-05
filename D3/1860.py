import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for testcase in range(1,T+1):
    temp = input().split(' ')
    while True:
        if '' in temp:
            temp.remove('')
        else:
            break
    N, M, K = map(int,temp)
    temp = input().split(' ')
    while True:
        if '' in temp:
            temp.remove('')
        else:
            break
    customer_list = sorted(list(map(int,temp)))
    for idx, time in enumerate(customer_list):
        if (time//M)*K >= (idx+1):
            pass
        else:
            answer = 'Impossible'
            break
    else:
        answer = 'Possible'
    print(f'#{testcase}',answer)