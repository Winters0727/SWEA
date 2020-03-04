import sys

sys.stdin = open('sample_input.txt')

def search(s, x, y, map_list):
    global dx, dy, cnt, count_list, answer, answer_count
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<= nx <= N-1 and 0<= ny <= N-1 and map_list[nx][ny] - s == 1:
            cnt += 1
            search(map_list[nx][ny], nx, ny, map_list)
    else:
        if cnt > answer_count:
            answer_count = cnt
            answer = s
        elif cnt == answer_count:
            if s < answer:
                answer = s
            
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    count_list = []
    answer, answer_count = N**2, 1
    for row in range(N):
        for col in range(N):
            cnt = 1
            start_point = num_list[row][col]
            search(start_point, row, col, num_list)
    print('#{0} {1} {2}'.format(tc, answer, answer_count))