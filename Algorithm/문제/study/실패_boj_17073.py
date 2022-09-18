import sys
sys.stdin = open("input.txt","r")

n, w = map(int,input().split())
visited = [0 for _ in range(n+1)]
link_list = []
leaf_node = 0

for i in range(n-1):
    first, second = map(int,input().split())
    link_list.append((first,second))

def node_bfs(w,node):
    global leaf_node, visited
    visited[node] = 1
    flag = 0

    for i in range(len(link_list)):
        first, second = link_list[i][0], link_list[i][1]
        if first == node and visited[second] == 0:
            node_bfs(w//2,i)
            flag = 1
        if second == node and visited[first] == 0:
            node_bfs(w//2,i)
            flag = 1

    if flag == 0:
        leaf_node +=1

node_bfs(w,1)
answer = round(w/leaf_node,4)
print(answer)




