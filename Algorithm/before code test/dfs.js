// 노드의 개수, 노드간의 연결관계(인접행렬), 방문여부 확인 visited, 순서를 프린트할 order
const n = 7
const adj = [[0,1,1,0,1,0,0],[0,0,0,1,0,1,0],[0,0,0,0,0,0,1],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
const visited = {}
const order = []


// // dfs logic by rec
// function dfs(node) {
//     visited[node] = 1
//     order.push(node+1)
//     for (let i=0; i<n; i++){
//         if (adj[node][i] === 1 && !visited[i]){
//             dfs(i)
//         }
//     }
// }
//
// dfs(0)
// console.log(order)



// dfs logic by loop
const stack = []
stack.push(0)

while (stack.length > 0){
    const node = stack.pop()
    if (!visited[node]) {
        visited[node] = 1
        order.push(node+1)
    }
    for (let i=0; i<n; i++){
        if (adj[node][i] === 1 && !visited[i]){
            stack.push(i)
        }
    }
}
console.log(order)