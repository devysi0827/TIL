from collections import deque
class Solution(object):
    def numIslands(self, grid):
        visited = []
        cnt = 0
        total_island = 0
        find_island = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    total_island += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and [i, j] not in visited:
                    stack = [[i, j]]
                    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                    while stack:
                        now_value = stack.pop()
                        x = now_value[0]
                        y = now_value[1]
                        for k in range(4):
                            dx = x + move[k][0]
                            dy = y + move[k][1]
                            if dx >= 0 and dx < m and dy >= 0 and dy < n and grid[dx][dy] == '1' and [dx,
                                                                                                      dy] not in visited:
                                visited.append([dx, dy])
                                stack.append([dx, dy])

                    cnt += 1
            if len(visited) == total_island:
                return cnt
        return cnt

