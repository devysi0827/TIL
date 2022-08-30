import sys
sys.stdin = open("input.txt","r")

def dfs(i,j):
    global visited, my_map
    house_cnt = 0
    move = [[1,0],[0,1],[-1,0],[0,-1]]
    stack = [[i,j]]
    while stack:
        x, y =stack.pop()
        house_cnt += 1
        for k in range(4):
            dx = x + move[k][0]
            dy = y + move[k][1]
            if dx<map_size and dy<map_size and dx>=0 and dy>=0 and my_map[dx][dy] == 1 and [dx,dy] not in visited:
                stack.append([dx,dy])
                visited.append([dx, dy])
    house_estate.append(house_cnt)

map_size = int(input())
my_map = []
for i in range(map_size):
    my_map.append(list(map(int,input())))

visited = []
house_estate = []
for i in range(map_size):
    for j in range(map_size):
        if my_map[i][j] == 1 and [i,j] not in visited:
            visited.append([i,j])
            dfs(i,j)

print(len(house_estate))
house_estate.sort()
for i in range(len(house_estate)):
    print(house_estate[i])


