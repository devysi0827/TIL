# 모던 자바스크립트 Deep Dive 17장 : 생성자 함수에 의한 객체 생성



```
const person = new Object();
```

생성자 함수(construnctor)란 new 연산자와 함께 호출하여 객체를 생성하는 함수를 말한다. 생성자 함수에 의해 생성된 객체를 인스턴스(instance)라 한다. 



일반적으로, 객체 리터럴 보다 훨씬 불편하지만 비슷한 객체를 여러 개 만들 때는 굉장히 편하다.

단, new 연산자 없이 사용할 경우 생성자 함수가 아닌 일반 함수 호출로 작동하니 유의하자.



### **생성자 함수의 인스턴스 생성 과정**

크게 두 가지로 나눌 수 있다.

인스터스의 생성과 초기화(초기값 할당)이다.

```
function Circle(radius) {
    this.radius = radius
    this.getDiameter = function () {
        return 2 * this.radius;
    };
}

const circle1 = new Circle(5) //Circle { radius: 5, getDiameter: [Function (anonymous)] }
```

이 예시처럼, this.radius에 매개변수를 대입함으로써 초기값 할당 과정은 이루어진다. 하지만, 인스턴스의 생성은 보이지 않는다. 그 이유는 new 생성자와 함께 생성자 함수를 호출하면 자바스크립트 엔진이 아래 과정을 거쳐 암묵적으로 인스턴스를 생성하고 초기화하여 반환하기 때문이다.



**1. 인스턴스 생성과 this 바인딩**

암묵적으로 빈 객체(인스턴스)가 생성된다. 이 인스턴스에 this가 바인딩된다. 이 과정은 런타임 이전에 실행된다.



※ 바인딩은 식별자와 값을 연결하는 과정을 의미한다. 



**2. 인스턴스 초기화**

생성자 함수가 한 줄씩 실행되어서 this가 바인딩되어있는 인스턴스를 초기화한다. 매개변수를 인스턴스의 프로퍼티로 넣거나 메서드를 할당한다.



**3. 인스턴스 반환**

완성된 인스턴스가 바인딩된 this가 암묵적으로 반환된다. 단, return이 있어도 return을 무시하고 this가 반환된다.



### **[[Call]] , [[Construct]]**

함수는 객체이므로 일반 객체와 동일하게 동작할 수 있다. 일반 객체가 가진 내부 슬롯과 메서드를 모두 가지고 있기 때문이다. 하지만, 일반 객체와는 다르다. 함수는 호출이 가능하기 때문이다. 그래서 함수 객체만을 위한 [[Enviroment]], [[Formal]], [[Parameters]] 등의 내부 슬롯과 [[Call]], [[Construct]] 같은 내부 메서드를 추가로 가지고 있다.



여기서 일반 함수라면, [[Call]]이 호출되고, new 연산자와 함께라면, 생성자 함수로서 호출되면 내부 매서드 [[Construct]]가 호출된다.

[사진사진]

이렇게 내부 메서드 [[Call]]을 갖는 함수 객체를 calllable이라 하며, 내부 메서드 [[Construct]]를 갖는 함수 객체를 constructor, 갖지 않는 함수를 non-constructor이라 부른다.  이 때, new 연산자로 함수를 호출하면 [[Construct]]가 호출되고, 일반 함수로 호출하면 [[Call]]이 호출된다.

constructor의 예시로는 함수 선언문, 함수 표현식, 클래스(클래스는 함수다)

non-constructor의 예시로는 메서드(ES6 축약표) ,화살표함수



new.target

생성자 함수가 new 없이 호출되는 것을 방지하기 위해 ES6에서는 new.target을 지원한다.

new.target은 this와 유사하게 construct인 모든 함수 내부에서 암묵적인 지역변수와 같이 사용되며 메타 프로퍼티라 부른다.



new 연산자와 함께 생성장 함수로서 호출되면 함수 내부의 new.target은 함수 자신을 가리킨다.

※ 일반 함수의 new.target은 undefined다.