import sys

sys.stdin = open('sample_input.txt')

def BFS(row, col, map_list, t):
    global R, C, answer, tunnel_list, visited
    visited[row][col] = 1
    queue = [[row, col]]
    while queue:
        r, c = queue.pop(0)
        answer += 1
        if visited[r][c] < t:
            for k in tunnel_list[map_list[r][c]]:
                n_r = r+dr[k]
                n_c = c+dc[k]
                if 0 <= n_r <= R-1 and 0 <= n_c <= C-1 and visited[n_r][n_c] == 0 and (k+2)%4 in tunnel_list[map_list[n_r][n_c]]:
                    visited[n_r][n_c] = visited[r][c] + 1
                    queue.append([n_r, n_c])

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
tunnel_list = [[], [0,1,2,3], [1,3], [0,2], [0,3], [0,1], [1,2], [2,3]]
T = int(input())
for tc in range(1, T+1):
    R, C, R_s, C_s, t = map(int,input().split())
    map_list = [list(map(int,input().split())) for _ in range(R)]
    visited = [[0 for _ in range(C)] for _ in range(R)]
    answer = 0
    BFS(R_s, C_s, map_list, t)
    print('#{0} {1}'.format(tc,answer))