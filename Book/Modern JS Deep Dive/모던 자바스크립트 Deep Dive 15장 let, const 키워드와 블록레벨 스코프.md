# **모던 자바스크립트 Deep Dive 15장 let, const 키워드와 블록레벨 스코프**



 ES5까지는 var로만 변수를 선언 가능했다. 하지만 이는 독특한 특징이 있어서 문제가 발생하기 쉬웠다.

\- 변수 중복 선언 가능으로 인한 의도치 않는 값 변경

\- 함수 외 모든 var 변수는 전역 변수로 취급되는 점 (함수 레벨 스코프와 전역 객체에 속함으로 인해 발생하는 문제)

\- 변수 호이스팅에 의해서 undefined가 반환될 수 있는 점

 

그래서 ES6부터는 let과 const가 도입되었다.

### **let**

\- 변수 중복 선언 금지 (syntax error 발생)

\- 블록 레벨 스코프 지원

\- 호이스팅이 안되는 것 처럼 처리 일시적 사각지대(Temporal Dead Zone)을 통해 에러 방지

 

위 두 줄은 이전 문서에서 알아봤지만 마지막 줄은 다시 알아보자.

```
console.log(foo); // undefined

var foo;
console.log(foo); // undefined

foo = 1
console.log(foo); // 1
```

이처럼 호이스팅이 일어나서, undefined가 불러오지는 게 우리가 배운 var이다.

 

```
console.log(foo); // Reference Error : fpp is not defined

let foo;
console.log(foo); // undefined

foo = 1
console.log(foo); // 1
```

하지만, let으로 할 경우 위처럼 달라진다. let은 "선언"과 "초기화 단계"가 분리되어 진행된다.

그래서 변수 호이스팅에 의해서 선언은 되었지만, 초기화가 일어나기 전에는 (변수 선언문에 도달하기 전에는) 참조 에러를 발생 시킨다.(초기화되지 않은 값을 사용할 수 있으니) 이 부분을 일시적 사각지대(Temporal Dead Zone, TDZ)라 부른다. 

**결론적으로, 호이스팅은 되나 호이스팅이 일어나지 않는 것처럼 동작한다.**

 

### **Const**

const는 let과 동일한 특징을 가진다. 하지만 다른 점이 있기에 그 부분을 중심으로 살핀다.

 

**- const는 반드시 선언과 동시에 초기화해야한다.**

```
 const foo = 1 //ok
 
 const foo; //SyntaxError
```

\- 재할당 금지 (상수기 때문에 TypeError가 발생한다.) 

=> 고정값으로 사용되어 유지보수성이 높아진다. 일반적으로 상수는 대문자로 작성하며 여러 단어의 경우 대문자 + 언더스코어(_)로 별도로 구분한다.

\- 재할당은 불가능하나 객체의 값은 바꿀 수 있다. **(상수는 불변이 아니다)**

```
const person = {
    name : 'lee'
}

person.name = 'kim'
```

이 경우 참조하는 값은 바뀌지 않는다.

 

결론적으로 말하면,

\- ES6 이후에는 이제 var을 사용하지 않는 걸 권장한다.

\- 일단 const를 사용한 후, 변경이 필요할 시 let으로 바꾸는 걸 권장한다.(상수가 더욱 안전하기 때문에)

