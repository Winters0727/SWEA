import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    start_idx = 0
    answer = -1
    while start_idx != len(num_list)-1:
        for idx in range(start_idx+1,len(num_list)):
            compare_num = str(num_list[start_idx]*num_list[idx])
            for i in range(len(compare_num)-1):
                if compare_num[i] > compare_num[i+1]:
                    break
            else:
                if int(compare_num) > answer:
                    answer = int(compare_num)
        start_idx += 1
    print('#{0} {1}'.format(tc,answer))