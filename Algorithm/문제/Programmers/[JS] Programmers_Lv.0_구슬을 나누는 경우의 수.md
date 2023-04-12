# **[JS] Programmers_Lv.0_구슬을 나누는 경우의 수**

### 문제

서로 다른 n개의 구슬을 고르는 방법입니다. (조합)

 

### 아이디어

1. 조합 공식을 구현한다.



![img](https://blog.kakaocdn.net/dn/bRFbOv/btr72oUE9u9/mJqblvBlsZFbVtmikFREVk/img.png)



 

### 구현(풀이)

```
function solution(balls, share) {
    var answer = 0;
    function factorial(n) {
        var x = BigInt(0)
        var y = BigInt(1)
        while (x < n) {
            x += BigInt(1)
            y *= x
        }
        return y
    }
    
    
    answer = factorial(balls) / (factorial(share) * factorial(balls-share))
    return answer;
}
```

별 거는 없었는데, 테스트케이스가 너무 커서 BigInt를 사용하지 않으면 오답으로 처리된다.

 

### 남의 풀이

```
const factorial = num => 
    Array
        .from({ length: num }, (_, i) => i + 1)
        .reduce((a, c) => a *= c, 1)

// const 팩토리얼 = (num) => num === 0 ? 1 : num * 팩토리얼(num - 1)

const solution = (n, m) => 
    Math.round(factorial(n) / (factorial(n - m) * factorial(m)))test
```

1. Array.from({length : num}, (_,i) => i +1 )은 `length: num` 부분은 길이에 맞는 n개의 undefined를 얇게 복사하여 새로운 Array를 만듭니다. 하지만 우리는 1부터 필요하므로 mapFn을 사용하여 i+1을 적용하여 [1,2, ... , n] 배열을 만들어줍니다.

2. 이후 리듀스 함수로 a값에 계속 곱해줘서 반환합니다. 

 

주석처리된 함수처럼 팩토리얼 함수를 재귀함수로 짤 수도 있습니다. 좋은 풀이라 가져왔습니다.

 

### 참고문서

https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from