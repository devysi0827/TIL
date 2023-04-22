# 모던 자바스크립트 Deep Dive 18장 : 함수와 일급 객체

아래 조건을 만족하는 객체를 **일급 객체**라 한다.

\1. 무명의 리터럴 생성할 수 있다. 즉, 런타임에 생성이 가능하다.

\2. 변수나 자료구조에 저장이 가능하다.

\3. 함수의 매개변수에 전달할 수 있다.

\4. 함수의 반환값으로 사용할 수 있다.



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