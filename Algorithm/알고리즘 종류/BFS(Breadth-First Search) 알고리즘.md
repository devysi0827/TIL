# **BFS(Breadth-First Search) 알고리즘**

### **BFS란?**

- 그래프 또는 트리를 얕은 단계부터 넓게 탐색하는 알고리즘이다. 주로 큐를 이용하여 구현하며 상세한 알고리즘에 따라 다를 수 있지만, 방문한 곳을 표시하지 않으면 무한루프 등에 빠질 수 있는 위험이 있다.
- 완전탐색의 일종이며, 모든 인접 지점을 차례로 방문한다.
- 대표적 예시로 네트워크 탐색, 최단 경로 문제 등이 있다.

![img](https://blog.kakaocdn.net/dn/bgK3lo/btskfXjsl7W/ApslSBJGln3K26NGeLoakK/img.gif)

### **BFS의 작동원리** 

\1. 중복방문을 체크할 visited 배열과 시작 노드를 큐에 넣는다.

\- node = 1, visit = {}, queue = [1]



\2. 가장 우선적으로 넣은 큐 값을 현재 노드로 사용한다. 그리고 현재 노드와 연결된 노드를 찾고, 모두 큐 안에 넣는다.

- **node** = 1, **Queue** = [2,3,4], **visit** = [1]

\3. 2를 반복한다.

- **node** = 2, **Queue** = [3,4,5], **visit** = [1,2]
- **node** = 3 **Queue** = [4,5,6,7], **visit** = [1,2,3]

   ...

\4. 모든 노드를 방문하면 종료한다.





### **BFS 코드**

```
const graph = [
    [0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
]

function bfs(startNode) {
    const q = []
    const visit = {}
    const order = []
    q.push(startNode)
    visit[startNode] = true
    while (order.length < graph.length){
        const curretTarget = q.shift()
        order.push(curretTarget+1)
        for (let i =0; i< graph[0].length; i++){
            if (graph[curretTarget][i] === 1 && !visit[i]){
                q.push(i)
                visit[i] = true
            }
        }
    }

    return order
}

console.log(bfs(0)) // [1, 2, 3, 4, 5 ,6, 7, 8, 9]
```



### **참고자료**

이미지출처 : **[https://medium.com/analytics-vidhya/a-quick-explanation-of-dfs-bfs-depth-first-search-breadth-first-search-b9ef4caf952c﻿](https://medium.com/analytics-vidhya/a-quick-explanation-of-dfs-bfs-depth-first-search-breadth-first-search-b9ef4caf952c)**