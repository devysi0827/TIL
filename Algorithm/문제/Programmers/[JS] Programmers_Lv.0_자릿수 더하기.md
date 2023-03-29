# **[JS] Programmers_Lv.0_자릿수 더하기**

### 문제

https://school.programmers.co.kr/learn/courses/30/lessons/120906

주어진 숫자의 각 자릿 수를 더해라.

 

### 아이디어

1. 주어진 숫자를 문자열로 만들어서 반복문을 돌리자.

2. 그리고 해당 문자열을 다시 숫자로 치환해서 answer에 합하자

 

### 구현(풀이)

```
function solution(n) {
    const stringNumber = n.toString()
    var answer = 0;
    
    for (var i=0; i< stringNumber.length; i++ ){
        answer += parseInt(stringNumber[i],10)
    }
    return answer;
}
```

 

### 남의 풀이

```
function solution(n) {
  return n
    .toString()
    .split("")
    .reduce((acc, cur) => acc + Number(cur), 0);
}
```

\- **obj.toString()** : 객체를 문자열로 바꾸어서 반환한다. ( ex. 12345 -> "12345")

\- **string.split()** : string을 separator을 기준으로 문자열을 나누어 담은 배열을 반환합니다. ( ex. "12345" -> ["1", "2", "3", "4", "5"])

\- **array.reduce()** : 배열의 각 요소에 대해서 콜백함수를 실행하여 하나의 함수를 반환합니다. callback, initialValue 로 초기값을 설정할 수 있습니다. ( ex. ["1", "2", "3", "4", "5"].reduce((acc, cur) => acc + Number(cur), 0) -> 10 )

 

### 참고문서

\- mdn, toStirng : https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/toString

\- mdn, reduce : https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce

\- mdn, split : https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString