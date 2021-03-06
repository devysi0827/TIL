import sys
sys.stdin = open("sample_input.txt","r")

#  함수
def enque(a):
    global rear
    rear += 1
    queue.append(a)

def deque():
    global front
    front += 1
    return queue.pop(0)

def find_loca(a):  #문자열 a가 어디 위치하고 있는지 알려준다
    for i in range(n):
        for j in range(n):
            if box[i][j] == a:
                loca =  i, j

    return loca

#  본문<-------------------->
case_num = int(input())  # 최초반복횟수
for case in range(case_num):
    # 기본 인풋을 이용한 박스형성
    n = int(input())
    box = []
    for i in range(n):
        temp = list(input())
        box.append(temp)

    # 시작점과 종료점 찾기
    ans = 0
    s_x, s_y = find_loca('2')
    g_x, g_y = find_loca('3')
    visited = [[False]*n for _ in range(n)]
    dis = [[0]*n for _ in range(n)]
    queue = [[s_x,s_y]]
    rear = -1
    front = -1
    #델타
    delta =[[0,-1],[-1,0],[1,0],[0,1]]
    while len(queue) >0:
        temp = deque()
        x = temp[0]
        y = temp[1]
        visited[x][y] = True
        if x == g_x and y == g_y:
            break
        for i in range(4):
            temp_ans = ans
            temp_x = x + delta[i][0]
            temp_y = y + delta[i][1]
            if temp_x >= 0 and temp_y >=0 and temp_x <= n - 1 and temp_y <= n - 1 and visited[temp_x][temp_y] == False and box[temp_x][temp_y] != '1':
                enque([temp_x,temp_y])
                dis[temp_x][temp_y] = dis[x][y] + 1

    if dis[g_x][g_y] == 0:
        dis[g_x][g_y] +=1
    print("#{} {}".format(case + 1, dis[g_x][g_y]-1))

