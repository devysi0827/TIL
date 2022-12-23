# **[python] Leetcode 79. Word Search**

https://leetcode.com/problems/word-search/

### **문제 소개**

- 그래프 내 알파벳이 연속으로 이어져서 찾는 단어가 될 수 있다면 True를 반환하는 문제

 

### **DFS(Graph Search) Algorithm**

```
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
```

- 알파벳의 첫글자가 일치하는 지 확인하고, 맞다면 dfs를 이용하여 주변을 탐색한다. 만약 있다면 true를 리턴한다.
- leetcode에서 word가 global로 사용되지가 않는다.. 이 부분에 대해서 좀 알아봐야겠다.