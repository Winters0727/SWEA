import sys

sys.stdin = open('sample_input.txt')

def game_act(board, act): # 3천자가 넘어가는데... 줄일 수 있는 방법이 없을까?
    y, x, c = map(int,act)
    board[x-1][y-1] = c
    if c == 1:
        op = 2
    elif c == 2:
        op = 1
    length = len(board)
    
    for col in range(1,y): # 가로 탐색
        if board[x-1][y-1-col] == 0:
            break
        elif board[x-1][y-1-col] == op:
            continue
        elif board[x-1][y-1-col] == c:
            for i in range(y-col,y-1):
                board[x-1][i] = c
            break

    for col in range(y,length):
        if board[x-1][col] == 0:
            break
        elif board[x-1][col] == op:
            continue
        elif board[x-1][col] == c:
            for i in range(y,col):
                board[x-1][i] = c
            break
            
    for row in range(1,x): # 세로 탐색
        if board[x-1-row][y-1] == 0:
            break
        elif board[x-1-row][y-1] == op:
            continue
        elif board[x-1-row][y-1] == c:
            for i in range(x-row,x-1):
                board[i][y-1] = c
            break

    for row in range(x,length):
        if board[row][y-1] == 0:
            break
        elif board[row][y-1] == op:
            continue
        elif board[row][y-1] == c:
            for i in range(x,row):
                board[i][y-1] = c
            break
    
    for num in range(1,length): # 대각선 탐색
        if (x-1+num) >= 0 and (x-1+num) <= length-1 and (y-1+num) >= 0 and (y-1+num) <= length-1:
            if board[x-1+num][y-1+num] == 0:
                break
            elif board[x-1+num][y-1+num] == op:
                continue
            elif board[x-1+num][y-1+num] == c:
                for i in range(1,num):
                    board[x-1+i][y-1+i] = c
                break

    for num in range(1,length):
        if (x-1+num) >= 0 and (x-1+num) <= length-1 and (y-1-num) >= 0 and (y-1-num) <= length-1:
            if board[x-1+num][y-1-num] == 0:
                break
            elif board[x-1+num][y-1-num] == op:
                continue
            elif board[x-1+num][y-1-num] == c:
                for i in range(1,num):
                    board[x-1+i][y-1-i] = c
                break

    for num in range(1,length):
        if (x-1-num) >= 0 and (x-1-num) <= length-1 and (y-1+num) >= 0 and (y-1+num) <= length-1:
            if board[x-1-num][y-1+num] == 0:
                break
            elif board[x-1-num][y-1+num] == op:
                continue
            elif board[x-1-num][y-1+num] == c:
                for i in range(1,num):
                    board[x-1-i][y-1+i] = c
                break

    for num in range(1,length):
        if (x-1-num) >= 0 and (x-1-num) <= length-1 and (y-1-num) >= 0 and (y-1-num) <= length-1:
            if board[x-1-num][y-1-num] == 0:
                break
            elif board[x-1-num][y-1-num] == op:
                continue
            elif board[x-1-num][y-1-num] == c:
                for i in range(1,num):
                    board[x-1-i][y-1-i] = c
                break
    return board

def game(N,M):
    board = [[0 for _ in range(N)] for _ in range(N)] # 먼저 NxN 보드를 0으로 초기화
    mid = int(N/2)
    board[mid-1][mid-1], board[mid-1][mid], board[mid][mid-1], board[mid][mid] = 2, 1, 1, 2 # 중앙에 기본 말 세팅
    game_flow = []
    for _ in range(M):
        game_flow.append(input().split())
    for act in game_flow: # 행동 명령어를 받을 때 마다 게임 진행 수행
        board = game_act(board, act)
    black, white = 0, 0
    for row in board: # 판 위의 검은 말, 흰 말 개수를 카운트
        black += row.count(1)
        white += row.count(2)
    return black, white

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    black, white = game(N,M)
    print('#{0}'.format(tc), black, white)