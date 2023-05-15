# Leetcode 70

### code

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let answer = [1,2]
    const dfs = (x) => {
        let k =2
        while (k <= n) {
            k +=1
            answer.push(answer[answer.length-1]+answer[answer.length-2] )
        } 
    }
    dfs(n)
    return answer[n-1]
};
```

