# **[js] Leetcode 70. Climbing Stairs**



### **문제**

[ Climbing Stairs - LeetCodeCan you solve this real interview question? Climbing Stairs - You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?  Example 1: Input: n = 2 Outpuleetcode.com](https://leetcode.com/problems/climbing-stairs/description/)

\- 계단을 1칸 또는 2칸씩 올라갈 수 있다. n개의 계단을 올라가는 모든 경우의 수를 구하여라

 

### **아이디어**

\1. 초항은 1칸을 오른다. 하나뿐이다. 이항은 1+1, 2로 두 가지로 고정되어 있다.

\2. 곰곰이 생각해보니, 루트는 무조건 두 가지로 고정된다. 

\- 2칸 전에서 2칸을 오른다.

\- 1칸 전에서 1칸을 오른다. (2칸전에서 1칸 오르고 다시 1칸 오르는 경우의 수는 이미 여기 포함되어있다.)

따라서, 2칸 전의 경우의 수 + 1칸 전의 경우의 수가 현재 칸에서의 총 경우의 수가 된다.

\3. 이를 수식으로 표현하면. dp[n] = dp[n-1] + dp[n-2] 로 표현할 수 있다.

 

### **구현(풀이)**

```
var climbStairs = function(n) {
    let dp = [1,2]
    const fillDP = (x) => {
        let k = dp.length
        while (k < n) {
            k +=1
            dp.push(dp[k-2]+dp[k-3] )
        } 
    }
    fillDP(n)
    return dp[n-1]
};
```

\1. 배열이 0 ~ n-1 이다보니 코드 상에서는 n-2, n-3으로 구현되었다.

\2. dp라는 배열(초기값 1,2)에 n이 나올때까지 반복문을 돌리면서 해당 계단에 필요수를 만든다.

\3. 마지막 값을 리턴한다.

### **남의 풀이**

```
var climbStairs = function(n) {

    if (n < 2) {
        return 1;
    }

    let firstStep = 1;
    let secondStep = 1;
    let thirdStep = 0;

    for (let i=2; i<=n; i++) {
        thirdStep = firstStep + secondStep;
        firstStep = secondStep;
        secondStep = thirdStep;
    }

    return thirdStep;
};
```

\- 나중에 알고보니 피보나치 수열이었다.

\- 속도는 비슷한데 배열을 사용하지 않으니 확실히 메모리 측면에서 차이가 났다. 현재 문제는 n이 45이하인데, 더 컸다면 더 큰 차이가 발생했을 거 같다.