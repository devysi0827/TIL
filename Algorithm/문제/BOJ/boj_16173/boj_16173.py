# 1. 세팅
n = int(input())
jelly_map = []
for i in range(n):
    temp_input = list(map(int, input().split()))
    jelly_map.append(temp_input)

# 2. 젤리 dfs
flag = -1
def dfs(num,x,y) :
    global flag
    if num == 0:
        return 0
    if x == n-1 and y == n-1:
        flag = 1
        return 0

    if x+num < n:
        dfs(jelly_map[x+num][y],x+num,y)
    if y+num < n:
        dfs(jelly_map[x][y+num],x,y+num)

dfs(jelly_map[0][0],0,0)

if flag == 1:
    print('HaruHaru')
else:
    print('Hing')
