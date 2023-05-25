# JS

### Slice

```
.slice(start,end)
```



### 동일배열 체크하는 법

```
```



### stack, queue 직접구현

```

```



### 기초 알고리즘

```
two-pointer
dfs
bfs
binary search
순열 / 조합
```





### 사칙연산

```
나눗셈(소수) : / 
반올림 : Math.round() , 0.5 기준
올림 : Math.ceil()
내림 : parseInt(문자열), Math.floor()
나머지 : %

- 배열 내 최소/ 최대
Math.min(...b)
Math.max(...b)
```



### DICT

```js
var dictObject = {}
/ Dictionary 추가, 제거
dictObject['elephant'] = '코끼리'; // 추가
delete dictObject['elephant']; // 삭제 (제대로 삭제 되면 true, 아니면 false)

// Dictionary 출력
for (var key in dictObject) {
    console.log("key : " + key +", value : " + dictObject[key]);
}

// 모든 key,value를 가져오는 방법
Object.keys(dictObject);
Object.values(dictObject)

// Dictionary 길이 구하는 방법
Object.keys(dictObject).length; // 3

// key를 체크하는 방법
"moneky" in dictObject // true
"elephant" in dictObject // false

// key의 마지막 값 가져오는 방법
var lastKey = Object.keys(dictObject)[Object.keys(dictObject).length - 1]
```



### 형변환

```
tostring()
parseInt()
```



### Array

```
push = append
pop = pop
shift = popleft
reverese = reverse


from = lambda
Array.from([1, 2, 3], x => x + x) : 유사배열객체를 배열로 만들어줌
[1,2,3].map(x => x + x) : 유사객체에서는 사용불가
```



### Sort

```
- 오름차순
arr.sort(function(a, b)  {
  return a - b;
});
```

https://hianna.tistory.com/409



### ETC

```
- matchAll
console.log(...str1.matchAll("number"))

- join
var b = [1, 5, 8, 3, 0];
var c = b.join(''"); // 15830

- split('')
var a = 15830;
var b = a.toString().split("");  // [1, 5, 8, 3, 0]
a.toString().split("").map(Number) // 숫자로 변환

- and = &&, or = ||
- false, true
```



### Input & Output

```
const readline = require("redaline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

rl.on("line", (line) => {
	/*입력받는 값을 처리하는 코드*/
	rl.close();
});

rl.on("close", () => {
	/*입력이 끝나고 실행할 코드*/
	process.exit();
});
```

