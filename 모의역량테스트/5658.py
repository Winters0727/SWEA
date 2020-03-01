import sys

sys.stdin = open('sample_input.txt')

def my_sort(a):
    for i in range(len(a)-1, -1, -1):
        for j in range(i):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def convert_num(hex_n):
    pow_n = len(hex_n) - 1
    result = 0
    for n in hex_n:
        if 65 <= ord(n) <= 70:
            temp = (ord(n) - ord('A') + 10) * (16 ** pow_n)
            result += temp
        else:
            temp = int(n) * (16 ** pow_n)
            result += temp
        pow_n -= 1
    return result

def rotate(num_input, k): # k : 0, 1, 2, …, b_n
    if k == 0:
        return num_input
    else:
        result = num_input[:]
        for _ in range(k):
            result = result[-1] + result[:-1]
        return result

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    num_input = input()
    b_n = N//4
    hex_list = []
    for k in range(b_n):
        rotate_input = rotate(num_input, k)
        temp_hex_list = [rotate_input[i:i+b_n] for i in range(0,N,b_n)]
        hex_list.extend(temp_hex_list)
    hex_list = set(hex_list)
    num_list = []
    for h_n in hex_list:
        num_list.append(convert_num(h_n))
    num_list = my_sort(num_list)
    answer = num_list[K-1]
    print('#{0} {1}'.format(tc,answer))