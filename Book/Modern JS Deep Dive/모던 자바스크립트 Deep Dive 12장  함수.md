# **모던 자바스크립트 Deep Dive 12장 : 함수**

### **함수란?**

함수는 자바스크립트의 핵심 개념이다. 또 다른 자바스크립트의 핵심 개념인 스코프, 실행 컨텍스트, 클로저, 생성자 함수에 의한 객체 생성, 메서드, this, 프로토타입, 모듈화 등이 모두 함수와 깊은 관련이 있다.

 

**함수는 일련의 과정을 문으로 구현하고 코드 블록으로 감써서 하나의 실행 단위로 정의**한 것이다.

매개변수, 인수, 반환값 등이 있으며 식별자인 함수 이름을 사용할 수 도 있다.

인수를 통해서 함수에 매개변수를 전달하고, 함수의 실행을 지시하는 것을 **함수의 호출**이라 한다.

```
function 함수이름 (매개변수1, 매개변수2, ...) {
	return 반환값
} // 함수정의

함수이름(인수1, 인수2) // 함수호출

// 예시
function add (x,y) {
	return x+ y
}

add(x,y) // 함수호출
```

 

### **함수를 사용하는 이유**

코드의 재사용을 할 수 있기 때문이다.

\- 유지보수의 편의성이 높아진다.

\- 코드의 신뢰성을 높여준다.

\- (함수명이 잘 지어졌다면) 코드의 가독성을 높여준다.

 

### **함수 리터럴**

객체, 숫자 처럼 함수도 리터럴로 사용할 수 있다.

리터럴은 약속된 기호 등을 통해서 값은 생성하기 위한 표기법이다. 즉, 함수 리터럴은 값은 생성하며, 이 값은 객체다.

즉, **함수는 객체다.** 

함수 객체는 일반 객체와 다르다. **일반 객체는 호출할 수 없지만, 함수는 호출할 수 있다**. 그리고 일반 객체에는 없는 함수 객체만의 고유한 프로퍼티를 갖는다.

 

### **함수 선언**

함수 선언은 네 가지 방식이 있다.

 

**함수 선언문**

```
function add (x,y) {
	return x+ y
}
```

함수 선언문은 함수 이름을 생략할 수 없으며. 표현식이 아닌 문이다. (평가되지만, undefined가 나온다.)

 

**함수 리터럴**

```
var myAdd = function add (x,y) {
    return x+ y
}
```

이처럼 함수를 리터럴로 사용하는 함수 표현식도 존재한다. (함수 표현식인 만큼 표현식인 문이다.)

그런데, 5장에서 우리는 변수에 표현식이 아닌 문을 할당할 수 없는 걸 알고 있다. ( ex. var foo = var x)

그러면 여기서는 왜 함수 선언문(표현식이 아닌 문)은 변수에 할당할 수 있는 걸까?

그 이유는 함수 선언문이 아니라 함수 리터럴을 할당 했기 때문이다. 함수 선언문과 리터럴이 동일하게 생겨서 생기는 오류로, {}가 코드 블록이 될 수도 있고, 객체 리터럴이 될 수도 있는 것처럼, 저 함수 선언문은 함수 리터럴이 될 수 있기도 하고, 함수 선언문이기도 하다. 이 경우 변수에 할당되었으므로 자바스크립트가 함수 리터럴로 판단한다.

 



![img](https://blog.kakaocdn.net/dn/cAmQtv/btr8KISoGp1/5g5An3ERj7f9bD6kXCyAcK/img.png)



 

그런데, 위 그림처럼 함수리터럴 표현식을 사용하고 변수에 할당하지 않으면 식별자가 없어서 함수를 호출할 수 없어진다. 그러면, 함수 선언문으로 선언한 함수는 왜 불러와지는가?

그들도 식별자가 없는 건 동일하다.

이 답은 자바스크립트 엔진이 암묵적으로 함수 이름과 같은 식별자를 생성하고 함수 객체를 할당해준다.

이 처럼 **값의 성질을 가지는 객체를 일급 객체**라 하며, 자바스크립트의 함수는 일급 객체이다.



![img](https://blog.kakaocdn.net/dn/SVLq6/btr8PY0GFrn/f3Vhsag2FmjfFD8TDI3kbk/img.png)



 

**함수 생성 시점과 호이스팅**

```
console.dir(add) //[Function : add]
console.dir(myAdd) // undefined

console.log(add(2,5)) // 7
console.log(myAdd(2,5)) // TypeError : myAdd is not a function

function add (x,y) {
    return x+ y
}

var myAdd = function add (x,y) {
    return x+ y
}
```

위 예시처럼, 함수 선언문은 호출할 수 있지만, 함수 표현식은 호출할 수 없다. 왜냐하면, 둘의 생성 시점이 다르기 때문이다.

 

**함수 선언문이 코드의 선두로 올려진 것처럼 동작하는 자바스크립트 고유의 특징을 함수 호이스팅이라 한다.**

선언과 할당의 타이밍이 다른 것처럼, 함수 선언문은 함수 호이스팅으로 호출이 가능하지만, 함수 표현식은 할당이 되지 않아 변수 호이스팅에 의해서 undefined가 나오게 된다.

**즉, 변수 할당문은 런타임에 평가되면서 함수 객체가 된다.**

함수 호이스팅은 함수를 호출하기 전에 반드시 함수를 선언해야한다는 규칙을 무시하기에 더글라스 크락포드는 함수 선언문 대신 함수 표현식을 사용할 것을 권장한다.

 

※ Function 생성자 함수와 관련된 내용은 생략한다. 일반적이지도 않고 바람직하기도 않기 때문이다.

 

**화살표 함수**

```
const myAdd = (x,y) => x+y;
```

간단하게 함수를 생성할 수 있지만 선언문과 할당식의 대체를 위해서가 아니며 기존 함수와 차이점이 있다.

생성자를 사용할 수 없으며, this 바인딩 방식이 다르고, prototype 프로퍼티가 없으며 arguments객체를 생성하지 않는다.

이 부분은 26절에 다시 상세하게 다룬다.

 

### **함수 호출**

함수를 호출하면 인수를 통해서 매개변수에 값을 전달한다.

이 때, 인수는 함수를 호출할 때 지정하며 개수나 값에 제한을 두지 않는다.

그리고 인수가 부족할 시, 해당 매개변수는 undefined로 초기화가 된다.

```
function add (x,y) {
    return x+ y
}

add(2,5) //7, 정상사용
add(2,5,10) // 7, 인수 초과사용 이 경우 뒤에 인수 무시
add(2) // NaN, 인수 부족, 2 + undefined = NaN
add('1', '2') //'12', 인수 타입 이상 예상 결과는 다르지만 함수는 동작함
```

그러다보니 위 예시처럼 다양한 문제가 발생한다.

이런 문제를 방지하려면 인수의 타입과 개수 확인 로직, 기본값 설정을 하면된다. (타입 스크립트를 사용하여서 정적 타입 검사를 하는 것도 방법이다.)

 

※ 초과된 함수는 버려지는 것이 아니라, arguments 객체에 저장된다. arguments 객체는 유사 배열 객체로 인수데이터들을 저장하고 있습니다.

 

**매개변수**

매개변수의 개수는 위에서 말했듯 제한을 두지는 않지만, 변수가 많을수록 코드를 유지보수 하기 어려워진다. **그러니 함수는 단 한가지 일만 해야하며, 매개변수는 가급적 적게 사용하자.**

함수 외부에서 내부로 전달한 객체를 함수 내부에서 변경하면, 함수 외부의 객체가 변경되는 부수 효과가 발생하는 것을 주의해야한다.

 

**반환문**

return을 통해서 함수의 실행 결과를 함수 외부로 반환할 수 있다.

return은 함수의 종료, 값의 반환 두 가지 역할을 수행한다.

만약, return 실행 이후에 오는 문들의 경우 무시가 되며, return값이 없다면 undefined가 자동으로 할당된다.

 

### **참조에 의한 전달(호출)**



![img](https://blog.kakaocdn.net/dn/cwKFKS/btr8ZUKcQAS/9AKkWF6ifZHtUeJS4PDdRk/img.png)



함수가 매개변수에 값을 전달하는 방식은 매개변수의 값에 따라서 다르다. 

만약, 그 값이 원시 값일 경우 값에 의한 전달(호출)로 그 값을 다른 곳에 재할당한다. 하지만, 객체일 경우 참조에 의한 전달(호출)로 그 주소값을 전달하여 매개변수를 수정하면 그 값이 수정되는 경우가 생긴다.

이는 예기치 못한 문제를 만들거나 상태 변화를 추적하기 어렵게 만들고 코드의 복잡성을 증가시키거나 가독성을 해치는 원인이 된다.

 

이와 같은 문제를 해결하려면 **옵저버 패턴**을 추가하는 등의 추가 대응을 하거나 deep copy를 통해서 불변 객체를 생성하는 방법이 있다.

 

※ 옵저버 패턴 : 객체의 상태 변화를 관찰하는 관찰자들, 즉 옵저버들의 목록을 객체에 등록하여 상태 변화가 있을 때마다 메서드 등을 통해 객체가 직접 목록의 각 옵저버에게 통지하도록 하는 디자인 패턴이다. 주로 분산 이벤트 핸들링 시스템을 구현하는 데 사용된다. 발행/구독 모델로 알려져 있기도 하다.



![img](https://blog.kakaocdn.net/dn/cXt0mD/btr8KLaI30n/IRfyTbk9V8dbIm2tMqOdt0/img.png)



\- Subject가 구독자 관리 / 변화알림 을 하는 주체 (우리가 흔히 쓰는 상태이다.)

\- Observer는 구독자들의 부모가 되는 추상 클래스 객체이다. subject의 값이 변화시 알림을 callback 받는다. 

\- Obsercer의 구체적인 구독자 객체들이다. 알림을 통해서 어떤 업데이트를 할 지 등은 정하면 된다. 

 

※ 순수 함수 : 외부 상태를 변경하지 도 않고 외부 상태에 의존하지도 않는 함수를 순수함수라 한다. 순수함수는 부수효과를 최대한 억제하기에 오류를 줄이고 안정성을 높이는 함수형 프로그래밍이다.

 

### **다양한 함수의 형태**

**즉시실행함수(IEF : Immediately Invoked Function Expression)**

즉시 실행 함수는 보통 무기명함수(기명도 가능하다)로 작성하며, 단 한 번만 호출되며 다시 호출할 수 없다.

즉시 실행 함수를 사용하면 불필요한한 변수나 함수가 적어지고 이들의 이름의 충돌을 방지할 수 있는 장점이 있다.

```
(function() {
   var a = 3
   var b = 5
   console.log( a+ b)
}())
```

위 예시처럼 반드시 그룹 연산자()로 감싸야하며 그렇지 않을 경우 에러가 발생한다.

왜냐하면, 그룹 연산자()로 감싸면서 함수리터럴로 평가가 되어서 함수객체가 생성할 수 있기 때문이다.

 

()로 감싸지 않은 무기명 함수는 함수 선언문의 문법과 다르기 때문에 에러가 발생한다.

만약, 기명이라 해도 함수 선언이 완료되어서 }부분에 ;이 자동으로 붙는데 여기서 ()은 단순한 그룹연산자로 취급되기에 에러가 난다.

 

그룹 연산자가 아니라 +나 ! 등으로 함수 객체만 만들 수 있다면 즉시실행함수로 사용가능하다. ()가 가장 일반적인 방법일 뿐이다

 

※ 그룹연산자 () 안에 아무것도 없으면 에러가 난다.

 

**재귀함수**

함수가 스스로를 호출하는 것은 재귀 호출(recursive call)이라 부른다. 재귀 함수는 자기 자신을 호출하는 행위, 즉 재귀 호출을 수행하는 함수를 말한다.

```
// 일반적인 반복 함수
function coundown(n) {
    for (var i=n; i>0; i--) console.log(i);
}

// 재귀 함수
function  countdownRecursive(n) {
    if (n==0) return
    console.log(n)
    countdownRecursive(n-1)
}
```

함수의 이름은 함수 몸체 내부에서만 유효하다. 그래서 함수 이름을 함수 내부에서 사용가능하다. 하지만 외부에서는 반드시 함수를 가리키는 식별자를 사용해야한다.

 

또한, 재귀 함수는 무한 호출이 될 수 있으므로 반드시 종료 조건을 넣어줘야한다. 재귀함수에 return문이 없었다면, -무한대까지 계속 반복하다가 스택오버플로 에러가 발생한다. 이런 점에서 코드를 직관적이고 간결하게 짤 수 있을 때만 잘 선택해서 사용해야한다.

 

**중첩함수**

함수 내부에 정의된 함수를 중첩 함수 또는 내부 함수라 한다. 그리고 중첩함수를 포함하는 함수를 외부함수라 부른다. 중첩 함수는 외부 함수 내부에서만 호출할 수 있다.

 

**콜백함수**

```
function repeat(n) {
    for (var i=0; i<n; i++) console.log(i)
}

function repeat2(n) {
    for (var i=0; i<n; i++) {
        if (i%2) console.log(i)
    }
}

repeat(3) // 0, 1, 2
repeat2(3) //
```

이 예시처럼, 전체적인 흐름은 똑같지만 함수의 일부분이 다르다면, 새로운 함수를 다시 정의해야한다.

이런 문제를 해결하는 방법은 함수를 합성하는 것이다. 변하지 않는 공통 로직을 정의하고, 변하는 부분은 함수 외부에서 내부로 전달하는 것이다.

 

```
function repeat(n,f) {
    for (var i=0; i<n; i++) f(i)
}

var logAll = function (i) {
    console.log(i)
}

var logOdds = function (i) {
    if(i%2) console.log(i)
    return 3
}

repeat(3,logAll) // 0,1,2
repeat(3,logOdds) // 1
```

 같은 결과지만 추상화된 함수를 전달받아서 수행하면서 하나의 함수로 더욱 유연하게 표현할 수 있게 되었다.

이처럼 함수의 **매개변수를 통해 다른 함수의 내부로 전달되는 함수를 콜백함수(callback function)라 한다**. 그리고 **매개 변수를 통해 함수의 외부에서 콜백 함수를 전달받은 함수를 고차 함수(Higher-Order Function HOF)라고 한다.**

즉, 고차함수는 콜백함수를 자신의 일부분으로 합성한다. 그리고 이 **고차함수가 콜백함수를 알맞은 시점에 호출한다.**

 

단, 콜백 함수의 매개변수로서 전달된 함수 리터럴은 고차 함수가 호출될 때마다 평가되어 함수 객체를 형성한다. 따라서 콜백함수가 만약 자주 사용한다면, 함수 외부에서 콜백 함수를 정의하는 것이 더 효율적이다.

 

콜백함수는 단순히 함수형 프로그래밍 패러다임 뿐만 아니라 비동기 처리와 배열 고차 함수에서 활용되는 중요한 패턴으로 잘 알아두어야한다.

 

※ 함수형 프로그래밍 패러다임에서는 매개변수를 통해서 함수를 받거나 반환값으로 함수를 주는 함수를 고차함수라 정의한다. 

 

**순수함수와 비순수함수**

순수함수 : 함수 외부와 관계없으며, 부수효과를 발생시키지 않음

비순수함수 : 함수 외부에 영향을 주며, 부수효과를 발생시킬 수도 있음

 

자바스크립트는 멀티 패러다임 언어이므로 이런 함수형 프로그래밍의 불변성과 안정성을 같이 추구한다.

 

※ 함수형 프로그래밍 :자료 처리를 수학적 함수의 계산으로 취급하고 상태와 가변 데이터를 멀리하는 프로그래밍 패러다임의 하나이다. 

 함수형 코드에서는 함수의 출력값은 그 함수에 입력된 인수에만 의존하므로 인수 x에 같은 값을 넣고 함수 f를 호출하면 항상 f(x)라는 결과가 나온다. 부작용을 제거하면 프로그램의 동작을 이해하고 예측하기가 훨씬 쉽게 된다. 이것이 함수형 프로그래밍으로 개발하려는 핵심 동기중 하나이다.

즉, 불변성을 지향한다.

 

 

참조

mdn 함수호출 : 

[ 함수 - JavaScript | MDN함수는 JavaScript에서 기본 구성 요소 중 하나입니다. JavaScript의 함수는 작업을 수행하거나 값을 계산하는 명령문의 집합인 프로시저(procedure)와 비슷하지만, 프로시저가 함수로 쓰이려면 입력을developer.mozilla.org](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions#함수_호출)

mdn, arguments object

[ The arguments object - JavaScript | MDNarguments is an array-like object accessible inside functions that contains the values of the arguments passed to that function.developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)

개발자 황준일 블로그 , observer pattern 구현

 

mdn, callback

[ Callback function - MDN Web Docs Glossary: Definitions of Web-related terms | MDNA callback function is a function passed into another function as an argument, which is then invoked inside the outer function to complete some kind of routine or action.developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function)

 

위키백과, 함수형 프로그래밍

[ 함수형 프로그래밍 - 위키백과, 우리 모두의 백과사전위키백과, 우리 모두의 백과사전. 함수형 프로그래밍(函數型 프로그래밍, 영어: functional programming)은 자료 처리를 수학적 함수의 계산으로 취급하고 상태와 가변 데이터를 멀리하는 프로그래밍ko.wikipedia.org](https://ko.wikipedia.org/wiki/함수형_프로그래밍)

 