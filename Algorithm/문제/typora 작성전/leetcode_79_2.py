class Solution(object):
    def exist(self, board, word):
        global answer
        def dfs(x, y, dfs_word,visited, word) :
            global answer
            move = [[1,0],[-1,0],[0,-1],[0,1]]
            if dfs_word == len(word)-1:
                answer = True
                return
            else:
                for i in range(4):
                    dx = x + move[i][0]
                    dy = y + move[i][1]
                    if 0<= dx < m and 0<= dy < n and visited[dx][dy] == 0 and board[dx][dy] == word[dfs_word+1]:
                        visited[dx][dy] = 1
                        dfs(dx,dy,dfs_word+1,visited,word)
                        visited[dx][dy] = 0

        m = len(board)
        n = len(board[0])
        visited = [[0] * n for _ in range(m)]
        answer = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    dfs(i,j,0,visited, word)
                    visited[i][j] = 0

        return answer