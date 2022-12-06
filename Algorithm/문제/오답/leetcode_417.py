from collections import deque



def pacificAtlantic(heights):
    global island_state, m, n, answer
    """
    "n" : no
    "b" : both
    "p" : pac
    "a" : atlantic
    """
    m = len(heights)
    n = len(heights[0])
    answer = []

    island_state = [["n"] * n for _ in range(m)]

    def checkIsland(i, j):
        global island_state, m, n, answer
        move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = [[0] * n for _ in range(m)]
        q = deque()
        q.append([i, j])
        visited[i][j] = 1
        p_flag = 0
        a_flag = 0

        while q:
            if p_flag == 1 and a_flag == 1:
                break
            x, y = q.popleft()
            for k in range(4):
                if p_flag == 1 and (k == 1 or k == 3):
                    continue
                if a_flag == 1 and (k == 0 or k == 2):
                    continue
                dx = x + move[k][0]
                dy = y + move[k][1]

                if 0 <= dx < n and 0 <= dy < m and island_state[dx][dy] == "a":
                    a_flag = 1
                elif 0 <= dx < n and 0 <= dy < m and island_state[dx][dy] == "p":
                    p_flag = 1
                elif 0 <= dx < n and 0 <= dy < m and island_state[dx][dy] == "b":
                    p_flag = 1
                    a_flag = 1

                if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == 0 and heights[dx][dy] <= heights[x][y]:
                    q.append([dx, dy])
                elif dx < 0 or dy < 0:
                    p_flag = 1
                elif dx >= n or dy >= m:
                    a_flag = 1

        if a_flag == 1 and p_flag == 1:
            island_state[i][j] = "b"
            answer.append([i, j])
            print("both", i, j)
            return
        elif a_flag == 1:
            island_state[i][j] = "a"
            print("a", i, j)
        elif p_flag == 1:
            island_state[i][j] = "p"
            print("p", i, j)
        else:
            print("n", i, j)

    for i in range(n):
        for j in range(m):
            checkIsland(i, j)

    return answer
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacificAtlantic(heights))




