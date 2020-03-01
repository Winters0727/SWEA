import sys

sys.stdin = open('sample_input.txt')

def cal(n1, n2, oper):
    if oper == '+':
        return n1 + n2
    elif oper == '-':
        return n1 - n2
    elif oper == '*':
        return n1 * n2
    elif oper == '/':
        return int(n1 / n2)

def DFS(n, k, oper_count):
    global oper_list, oper_num, oper_used, opers, num_list, ans_max, ans_min
    if n == k:
        re_num = num_list[::-1]
        re_opers = opers[::-1]
        while re_opers:
            n1, n2 = re_num.pop(), re_num.pop()
            oper = re_opers.pop()
            result = cal(n1, n2, oper)
            re_num.append(result)
        ans_temp = re_num.pop()
        if ans_temp < ans_min:
            ans_min = ans_temp
        if ans_temp > ans_max:
            ans_max = ans_temp
    else:
        for idx in range(4):
            if oper_count[idx] != oper_used[idx]:
                opers[n] = oper_list[idx]
                oper_used[idx] += 1
                DFS(n+1, k, oper_count)
                oper_used[idx] -= 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    oper_list = ['+', '-', '*', '/']
    oper_count = list(map(int,input().split()))
    oper_num = sum(oper_count)
    num_list = list(map(int,input().split()))
    oper_used = [0 for _ in range(4)]
    opers = [0 for _ in range(oper_num)]
    ans_max, ans_min = -100000000, 100000000
    DFS(0, oper_num, oper_count)
    print('#{0} {1}'.format(tc, ans_max-ans_min))