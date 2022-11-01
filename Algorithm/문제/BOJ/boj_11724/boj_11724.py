m, n = map(int, input().split())
node_map = [[0] * (m+1)  for _ in range(m+1)]
for i in range(n):
    temp_x, temp_y = map(int, input().split())
    node_map[temp_x][temp_y] = 1
    node_map[temp_y][temp_x] = 1
visited = [0] * (m+1)
count = 0

def dfs(k,level) :
    global count
    if level == 0 and visited[k] == 0:
        count += 1
    visited[k] = 1
    for i in range(m+1):
        if node_map[k][i] == 1 and visited[i] == 0:
            dfs(i,level+1)

for i in range(1,m+1):
    if visited[i] == 0:
        dfs(i,0)
print(count)