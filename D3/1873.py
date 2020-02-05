import sys

sys.stdin = open('sample_input.txt')

def check_plain(map_list, plain_idx):
    if map_list[plain_idx[0]][plain_idx[1]] == '.':
        return True
    return False

def move(map_list, tank_idx, command):
    if command == 'U':
        move_idx = (tank_idx[0]-1,tank_idx[1])
        if tank_idx[0]-1 >=0 and check_plain(map_list,move_idx):
            map_list[tank_idx[0]][tank_idx[1]] = '.'
            tank_idx = move_idx
            map_list[tank_idx[0]][tank_idx[1]] = '^'
        else:
            map_list[tank_idx[0]][tank_idx[1]] = '^'
    elif command == 'D':
        move_idx = (tank_idx[0]+1,tank_idx[1])
        if tank_idx[0]+1 < row and check_plain(map_list,move_idx):
            map_list[tank_idx[0]][tank_idx[1]] = '.'
            tank_idx = move_idx
            map_list[tank_idx[0]][tank_idx[1]] = 'v'
        else:
            map_list[tank_idx[0]][tank_idx[1]] = 'v'
    elif command == 'L':
        move_idx = (tank_idx[0],tank_idx[1]-1)
        if tank_idx[1]-1 >=0 and check_plain(map_list,move_idx):
            map_list[tank_idx[0]][tank_idx[1]] = '.'
            tank_idx = move_idx
            map_list[tank_idx[0]][tank_idx[1]] = '<'
        else:
            map_list[tank_idx[0]][tank_idx[1]] = '<'
    elif command == 'R':
        move_idx = (tank_idx[0],tank_idx[1]+1)
        if tank_idx[1]+1 < col and check_plain(map_list,move_idx):
            map_list[tank_idx[0]][tank_idx[1]] = '.'
            tank_idx = move_idx
            map_list[tank_idx[0]][tank_idx[1]] = '>'
        else:
            map_list[tank_idx[0]][tank_idx[1]] = '>'
    return map_list, tank_idx

def shoot(map_list, tank_idx):
    if map_list[tank_idx[0]][tank_idx[1]] == '^':
        for i in range(tank_idx[0]-1,-1,-1):
            if map_list[i][tank_idx[1]] == '*':
                map_list[i][tank_idx[1]] = '.'
                break
            elif map_list[i][tank_idx[1]] == '#':
                break
    elif map_list[tank_idx[0]][tank_idx[1]] == 'v':
        for i in range(tank_idx[0]+1,row):
            if map_list[i][tank_idx[1]] == '*':
                map_list[i][tank_idx[1]] = '.'
                break
            elif map_list[i][tank_idx[1]] == '#':
                break
    elif map_list[tank_idx[0]][tank_idx[1]] == '<':
        for i in range(tank_idx[1]-1, -1, -1):
            if map_list[tank_idx[0]][i] == '*':
                map_list[tank_idx[0]][i] = '.'
                break
            elif map_list[tank_idx[0]][i] == '#':
                break
    elif map_list[tank_idx[0]][tank_idx[1]] == '>':
        for i in range(tank_idx[1]+1, col):
            if map_list[tank_idx[0]][i] == '*':
                map_list[tank_idx[0]][i] = '.'
                break
            elif map_list[tank_idx[0]][i] == '#':
                break
    return map_list

def game_start(map_list, tank_idx, command):
    for cmd in command:
        if cmd == 'S':
            map_list = shoot(map_list,tank_idx)
        else:
            map_list, tank_idx = move(map_list, tank_idx, cmd)
    return map_list, tank_idx

T = int(input())
for testcase in range(1, T+1):
    temp = input().split(' ')
    while temp:
        if '' in temp:
            temp.remove('')
        else:
            break
    row, col = map(int,temp)
    map_list = [] # 맵 생성
    for _ in range(row):
        map_list.append(list(input().strip()))
    tank_motion = ['<','>','v','^']
    tank_idx = 0
    for i in range(row):
        for j in range(col):
            if map_list[i][j] in tank_motion:
                tank_idx = (i,j)
                break
        if tank_idx:
            break
    W = int(input().strip())
    command = input()
    map_list, tank_idx = game_start(map_list, tank_idx, command)
    print(f'#{testcase}',end = ' ')
    for m in map_list:
        print(''.join(m))