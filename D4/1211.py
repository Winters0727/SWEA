import sys

sys.stdin = open('sample_input.txt')

def moving(start_node, labyrinth): # 이동 우선 순위는 좌/우가 먼저이고 그 다음이 아래
    start_idx = [0,start_node] # 좌/우 간에 우선 순위가 필요하다면 코드를 바꿔야한다.
    mv_cnt = 0
    move = None
    while start_idx[0] != 99: # 바닥 인덱스 99에 도달할 때까지
        if move == None: # 내려가고 있을 때
            if (start_idx[1]+1) < 100 and labyrinth[start_idx[0]][start_idx[1]+1] == '1':
                start_idx[1] += 1
                move = 'right'
                mv_cnt += 1
            elif (start_idx[1]-1) > 0 and labyrinth[start_idx[0]][start_idx[1]-1] == '1':
                start_idx[1] -= 1
                move = 'left'
                mv_cnt += 1
            elif labyrinth[start_idx[0]+1][start_idx[1]] == '1':
                start_idx[0] += 1
                mv_cnt += 1
        elif move == 'right': # 오른쪽으로 이동할 때
            if labyrinth[start_idx[0]+1][start_idx[1]] == '0':
                start_idx[1] += 1
                mv_cnt += 1
            elif labyrinth[start_idx[0]+1][start_idx[1]] == '1':
                start_idx[0] += 1
                mv_cnt += 1
                move = None
        elif move == 'left': # 왼쪽으로 이동할 때
            if labyrinth[start_idx[0]+1][start_idx[1]] == '0':
                start_idx[1] -= 1
                mv_cnt += 1
            elif labyrinth[start_idx[0]+1][start_idx[1]] == '1':
                start_idx[0] += 1
                mv_cnt += 1
                move = None
    return mv_cnt
        
        
for tc in range(1,11):
    N = int(input())
    labyrinth = []
    for _ in range(100):
        labyrinth.append(input().split())
    col_list = [idx for idx in range(100) if labyrinth[0][idx] == '1'] # 첫 줄의 시작 포인트를 리스트로 묶음
    answer = 0
    min_cnt = 10000
    for col in col_list:
        moving_cnt = moving(col, labyrinth)
        if moving_cnt < min_cnt:
            min_cnt = moving_cnt
            answer = col
        elif moving_cnt == min_cnt and col > answer:
            answer = col
    print('#{0}'.format(tc),answer)