# **모던 자바스크립트 Deep Dive 10장 : 객체 리터럴**

### **객체**

자바스크립트는 객체 기반 언어이며, 자바스크립트를 구성하는 거의 모든 것이 객체(함수, 배열, 정규 표현식)다.

 

원시 타입은 하나의 값만 나타내고 변경이 불가능하지만 객체 타입은 다양한 타입의 값을 하나의 단위로 구성한 복합적인 자료구조이며 변경이 가능하다.

 

**프로퍼티와 메서드**

객체는 0개 이상의 프로퍼티로 구성된 집합이다.

**프로퍼티**는 키와 값으로 구성된 객체의 상태를 나타내는 값(데이터)이다.

자바스크립트에서 사용할 수 있는 모든 값은 프로퍼티 값이 될 수 있다.

자바스크립트의 함수는 일급 객체이므로 값으로 취급할 수 있다. 이 때, 프로퍼티 값이 함수일 경우 이를 **메서드**라 부른다.

이렇게 객체의 집합으로 프로그램을 표현하려는 프로그래밍 패러다임을 **객체지향 프로그래밍**이라 한다.

 

※ 일급객체(First-class Object)란 다른 객체들에 일반적으로 적용 가능한 연산을 모두 지원하는 객체를 가리킨다. [위키백과] : mdn 일급 함수에서 일급 객체의 정의는 위키백과를 참조한다... 진짜다.

> 일급함수의 특징 : 함수를 변수처럼 다를 수 있다.
>
> - 변수에 할당(assignment)할 수 있다.
> - 다른 함수를 인자(argument)로 전달 받는다.
> - 다른 함수의 결과로서 리턴될 수 있다.

 

### **객체 리터럴**

C++이나 Java 같은 클래스 기반 객체지향 언어는 클래스를 사전에 정의하고 필요한 시점에 new 연산자와 함께 생성자를 호출하여 인스턴스를 생성하는 방식으로 객체를 생성한다.

 

자바스크립트는 프로토타입 기반 객체지향 언어로서 클래스 기반과 다르게 다양한 객체 생성 방법을 지원한다.

\- 객체 리터럴 : {}로 직접 선언하는 방식

\- Object 생성자 함수

\- 생성자 함수

\- Object.create 메서드

\- Class(ES6)

 

※ 클래스 : 인스턴스를 만들기 위한 템플릿의 역할

※ 인스턴스 : 객체가 메모리에 저장되어 실제로 존재하는 것

※ 코드 블록과 객체 리터럴의 중괄호는 다르다. 그렇기 때문에 객체 리터럴 뒤에는 종결을 의미하는 세미 콜론을 붙인다.

 

### **프로퍼티**

**객체는 프로퍼티의 집합이며, 프로퍼티는 키와 값으로 구성된다.**

프로퍼티 키: 빈 문자열을 포함하는 모든 문자열 또는 심벌 값

프로퍼티 값: 자바스크립트에서 아용 가능한 모든 값

키는 식별자의 역할을 하는데, 식별자 네이밍 규칙을 따를 필요는 없지만 따를 경우 '' 없이 써도 괜찮다.

```
var person = {
    firstName : 'seo', // 따른 경우
    'last-name' : 'lee', // 따르지 않은 경우 ''를 붙여야함.   
}
```

또한, 프로퍼티 키로 사용할 표현식을 동적으로 사용할 수 있다. 이 경우 대괄호를 사용한다.

```
var obj = {};
var key = 'hello';

obj[key] = 'world'; // 프로퍼티 값 생성
console.log(obj); // {hello: "world"}

obj[key] = 'hello'; // 프로퍼티 값 갱신
console.log(obj); // {hello: "hello"}
```

빈 문자열도 프로퍼티의 키로 가능하며, 숫자도 가능하다. 단, 숫자는 자동으로 문자열로 변환된다.

이미 존재하는 프로퍼티의 키를 중복 선언하면 덮어쓰며 별도의 에러는 발생하지 않는다.
이 때, 함수가 프로퍼티의 값일 경우 이를 메서드라 표현한다.

delete 식별자를 이용하여 제거할 수 있으며, 만약 없는 키워드에 사용할 경우 아무런 일이 발생하지 않는다(에러도 없다)

 

### **프로퍼티 접근**

프로퍼티를 접근하는 방법은 크게 두 가지가 있다.

\- 마침표 프로퍼티 접근 연산자(.)을 사용하는 **마침표 표기법(dot notation)**

\- 대괄호 프로퍼티 접근 연사자([...])을 사용하는 **대괄호 표기법(bracket notation)**

```
var person = {
    name : 'Lee',
    'first-name' : 'sell'
}

console.log(person.name) // Lee
console.log(person['name']) // Lee
console.log(person[name]) // ReferenceError : name is not defined
console.log(person['names']) // undefined

console.log(person.'last-name') // syntax Error
console.log(person.last-name) // Broswer : NaN or Node.js : ReferenceError
console.log(person['last-name']) // sell
```

**이 때, 대괄호 표기법은 반드시 따옴표로 감싼 문자열이여야한다.**

그렇지 않을 경우 식별자로 취급하여 문자열 name 이 아닌 식별자 name을 찾고, 찾지 못해서 Error를 발생시킨다.

하지만, 없는 문자열을 입력할 경우 Error 없이 undefined를 반환하니 조심하자.
또한, **대괄호 표기법은 식별자 네이밍 규칙을 따르지 않아도 접근이 가능하나, 마침표 표기법은 그렇지 않으니 조심하자**

 

※ person.last-name에서 person.last에서 last를 찾고 undefined가 나오게 된다. 그리고 undefined -name 에서 다시 name을 찾게된다. 이 때, Broswer는 window에 name이라는 전역변수가 존재하고 Node는 없기 때문에 둘이 다른 반응이 나오게 된다.

위 코드를 조금 독특하게 변형하면 person.first('10') - name('1') 에서 암묵적 타입 변환이 일어나서 9가 반환된다.

```
var person = {
    name : 'Ho',
    'first-name' : 'Lee',
    first : '10'
}

var name = '1'

console.log(person.first-name) // 9
```

 

### **ES6 객체 리터럴 확장 기능**

ES6에서 확장 기능을 제공한다.

 

**축약기능**

```
//ES5
var x=1, y=2;
var obj = {
	x: x,
    y: y
};

//ES6
let x= 1, y=2;
const obj = {x,y};
```

 

**프로퍼티 동적 생성**

```
//ES5
var prefix = 'prop';
var i = 0;
var obj = {};

obj[prefix + '-' + ++i] = i;
obj[prefix + '-' + ++i] = i;
obj[prefix + '-' + ++i] = i;
console.log(obj) //{ 'prop-1': 1, 'prop-2': 2, 'prop-3': 3 }

//ES6
const prefix = 'prop';
let i = 0;
const obj = {
    [`${prefix}-${++i}`] : i,
    [`${prefix}-${++i}`] : i,
    [`${prefix}-${++i}`] : i,
};
console.log(obj) //{ 'prop-1': 1, 'prop-2': 2, 'prop-3': 3 }
```

 

**메서드 축약**

```
// ES5
var obj = {
    name: 'Lee',
    sayHi : function() {
        console.log('Hi!' +this.name);
    }
}

// ES6
const obj = {
    name: 'Lee,
    sayHi() {
        console.log('Hi' +this.name);
    }
}
```

단, 이렇게 축약표현으로 정의한 메서드는 프로퍼티에 할당한 함수와 다르게 작동한다.

 

※ 이 때 차이점은 인스턴스를 생성할 수 없는 non-construct로 바뀐다는 점이다. 자세한 내용은 26절에서 다시 서술하겠다.

 

### 참조

일급 객체 위키 백과 : [https://ko.wikipedia.org/wiki/%EC%9D%BC%EA%B8%89_%EA%B0%9D%EC%B2%B4](https://ko.wikipedia.org/wiki/일급_객체)