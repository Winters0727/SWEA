import sys

sys.stdin = open('sample_input.txt')

def and_num(num):
    n = 0
    while True:
        n += 1
        summation = n*(n+1)/2
        if summation >= num:
            n -= 1
            break
    p = num - n*(n+1)/2
    result_point = (p, n+2-p)
    return result_point

def sharp_num(num_tuple):
    p,q = num_tuple
    n = (p+q)-2
    start_num = n*(n+1)/2 + 1
    result = start_num + p -1
    return result
    
def star_num(p,q):
    p_num, q_num = and_num(p), and_num(q)
    result = sharp_num((p_num[0]+q_num[0], p_num[1]+q_num[1]))
    return int(result)

T = int(input())

for testcase in range(1,T+1):
    temp = input().split(' ')
    while True:
        if '' in temp:
            temp.remove('')
        else:
            break
    p,q = map(int,temp)
    print(f'#{testcase}',star_num(p,q))