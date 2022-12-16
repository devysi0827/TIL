class Solution(object):
    from collections import deque
    def findCircleNum(self, isConnected):
        visited = []
        q = deque()
        n = len(isConnected)
        cnt = 0
        for city in range(n):
						# bfs!
            if city not in visited:
                cnt += 1
                q.append(city)
                if city == 0:
                    visited.append(0)
                while q:
                    city_num = q.popleft()
                    for i in range(n):
                        if isConnected[city_num][i] == 1 and i not in visited:
                            visited.append(i)
                            q.append(i)
        return cnt