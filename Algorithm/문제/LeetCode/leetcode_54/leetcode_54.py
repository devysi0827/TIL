class Solution(object):
    def spiralOrder(self, matrix):
        if len(matrix[0]) == 1 and len(matrix) == 1:
            return [matrix[0][0]]
        movement = [[0,1], [1,0], [0,-1], [-1,0]]
        m = len(matrix)
        n = len(matrix[0])
        visited = [[0] * n for _ in range(m)]
        direction = 0
        x = 0
        y = 0
        visited[x][y] = 1
        answer = []
        answer.append(matrix[x][y])

        while direction >= 0:
            dx = x + movement[direction][0]
            dy = y + movement[direction][1]

            if 0 <= dx <m and 0<= dy < n and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                x = dx
                y = dy
                answer.append(matrix[x][y])
            else:
                if direction == 3:
                    direction = 0
                else:
                    direction +=1
                dx = x + movement[direction][0]
                dy = y + movement[direction][1]
                if 0 <= dx <m and 0<= dy < n and visited[dx][dy] == 1:
                    direction = -1

        return answer