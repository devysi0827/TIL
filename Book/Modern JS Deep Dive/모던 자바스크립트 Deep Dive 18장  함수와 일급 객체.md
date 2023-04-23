# 모던 자바스크립트 Deep Dive 18장 : 함수와 일급 객체

아래 조건을 만족하는 객체를 **일급 객체**라 한다.

1. 무명의 리터럴 생성할 수 있다. 즉, 런타임에 생성이 가능하다.

2. 변수나 자료구조에 저장이 가능하다.

3. 함수의 매개변수에 전달할 수 있다.

4. 함수의 반환값으로 사용할 수 있다.

 

자바스크립트 함수는 이전 장에서 살펴본 것처럼 이 조건을 모두 만족하므로 일급 객체이다.

함수가 일급 객체라는 것은 함수를 객체와 동일하게 사용 가능하다는 것이다. 

그래서, 함수는 값을 사용할 수 있는 곳 어디서든 리터럴로 정의할 수 있으며, 런타임에 함수 객체로 평가된다.

또한, 일급 객체로서 함수가 가지는 가장 큰 특징은 매개변수와 반환값으로 사용이 가능하다는 점이다. 이는 함수형 프로그래밍을 가능케 하는 자바스크립트의 장점 중 하나이다.

 

### **함수 객체의 프로퍼티**

단, 함수와 객체는 다르다. 일반 객체는 없고, 함수만이 가지는 고유의 프로퍼티가 존재한다.

getOwnPropertyDescriptors를 이용해 알아보자

```
function Circle(radius) {
    if (!new.target)
        return new Circle(radius)
    this.radius = radius
    this.getDiameter = function () {
        return 2* this.radius
    }
}
console.log(Object.getOwnPropertyDescriptor(Circle))
console.log(Object.getOwnPropertyDescriptor(Circle, '__proto__'))

// 결과값
{
  length: { value: 1, writable: false, enumerable: false, configurable: true },
  name: {
    value: 'Circle',
    writable: false,
    enumerable: false,
    configurable: true
  },
  arguments: {
    value: null,
    writable: false,
    enumerable: false,
    configurable: false
  },
  caller: {
    value: null,
    writable: false,
    enumerable: false,
    configurable: false
  },
  prototype: { value: {}, writable: true, enumerable: false, configurable: false }
}
```

위에 arguments, calller ,length, name, prototype은 모두 함수 객체의 데이터 프로퍼티로, 일반 함수에는 없는 함수 객체 고유의 프로퍼티이다. 

하지만, 마지막 줄에 __proto__는 접근자 프로퍼티이며, 함수 고유의 프로퍼티가 아니라 Object.prototype 객체의 프로퍼티를 상속받은 것이다. __proto__ 접근자 프로퍼티는 모든 객체가 사용할 수 있다.

 

이제 각 개체를 알아보도록하자.

 

### **arguments**

arguments 객체는 함수 호출 시 전달된 인수들의 정보를 담고 있는 순회 가능한 유사 배열 객체이며, 함수 내부의 지역 변수처럼 사용된다.

arguments 함수는 주로 매개변수 개수를 확정할 수 없는 가변 인자 함수를 구현할 때 유용하다.

 

```
function sum() {
    let res = 0;
    for (let i = 0; i <arguments.length; i++){
        res += arguments[i];
    }
    return res;

}

console.log(sum(1,2,3,4)) //10
```

 

ES6부터는 Rest 파리미터(...args)의 도입으로 더 쉽게 작성할 수 있다.

```
function sum(...args) {
    return args.reduce((ans, cur) => ans+cur,0)
}

console.log(sum(1,2,3,4))
```

 

※ arguments는 유사 배열 객체이므로, for문은 돌 수 있지만, 배열 메서드는 사용할 수 없거나 간접 호출을 진행해야한다.

※ symbol 프로퍼티는 arguments 객체를 순회 가능한 자료구조인 이터러블을 만들 수 있다.

 

 

### **Caller**

caller는 자신을 호출한 함수를 가리킨다. 

이 함수는 EMCAScript에서 표준화 되지 않았으며, 아마 앞으로도 안 될 것이다.

```
function foo(func) {
    return func()
}

function bar() {
    return 'caller:' + bar.caller;
}

console.log(foo(bar))
console.log(bar())

// 결과
caller:function foo(func) ... 생략
node => caller:function (exports, require, module, __filename, __dirname) ... 생략
broswer => caller: null
```

이처럼 자신을 부른 함수를 부른다. 

만약, 최상단 함수일 경우 broser는 null이지만, 노드는 자신을 부른 모듈(파일)을 부른다.

 

### **length**

arguments의 개수, 길이를 의미한다.

 

### **name**

ES6에서 표준이 된다. 함수의 이름을 나타낸다.

기명함수는 함수의 이름을, 익명 함수는 함수를 가리키는 변수명을 나타낸다. 

 

 

### **__proto__**

내부 슬롯에 직접 접근은 불가능하지만 __proto__를 통하여 간접적으로 객체에 접근할 수 있다.

 

### **prototype** 

constructor인 함수만이 가지는 프로퍼티이다.

non-constructor는 prototype이 없다.

 

 

__proto__와 prototype의 관계는 매우 복잡하다. 이를 여기 적기에 너무 칸이 적은 것 같고, 마침 바로 뒤 단원이 이 내용이니 내일 추가로 서술하기로 한다.