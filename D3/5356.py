import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    words = []
    max_len = 0
    for _ in range(5):
        temp = list(input())
        if len(temp) > max_len:
            max_len = len(temp)
        words.append(temp)
    for e in words:
        if len(e) < max_len:
            for _ in range(max_len-len(e)):
                e.append('')
    answer = ''
    for i in range(max_len):
        for j in range(5):
            answer += words[j][i]
    print('#{}'.format(tc),answer)