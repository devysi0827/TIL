import sys
sys.stdin = open("input.txt","r")

n = int(input())
chess_map = [[0 for i in range(n)] for j in range(n)]

def check_queen(x,y,chess_map):
    move = [[-1, -1], [0, -1], [1, -1]]

    for i in range(3):
        while x >= 0 or y >= 0:
            dx = x + move[i][0]
            dy = y + move[i][1]
            if dx >=0 and dy >= 0 and chess_map[dx][dy] == 1:
                return False
    return True




cnt = 0
def dfs(dfs_cnt,chess_map):
    global cnt

    if dfs_cnt == n:
        cnt += 1
    else:
        for i in range(n):
            flag = check_queen(i,dfs_cnt,chess_map)

            if flag:
                new_chess_map = list(chess_map)
                new_chess_map[i][dfs_cnt] = 1
                dfs(dfs_cnt+1,new_chess_map)


dfs(0,chess_map)