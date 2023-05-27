// problem
const n = 6
const adj = [[0,1,1,0,0,0],[1,0,0,1,1,0],[1,0,0,0,0,1],[0,1,0,0,0,0],[0,1,0,0,0,1],[0,0,1,0,1,0]]
const order = [] // 순서 찾기 문제 변형

// dfs
const visited = {}

// dfs logic by rec
function dfs(node) {
    visited[node] = 1
    order.push(node)
    for (let i=0; i<n; i++){
        if (adj[node][i] === 1 && !visited[i]){
            dfs(i)
        }
    }
}

// dfs(0)

// dfs logic by loop
const stack = []
stack.push(0)

while (stack.length > 0){
    const node = stack.pop()
    if (!visited[node]) {
        visited[node] = 1
        order.push(node)
    }
    for (let i=0; i<n; i++){
        if (adj[node][i] === 1 && !visited[i]){
            stack.push(i)
        }
    }
}
console.log(order)