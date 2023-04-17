# **모던 자바스크립트 Deep Dive 16장 : 프로퍼티 어트리뷰트**

### **내부 슬롯과 내부 메서드**

이 장을 설명하기 앞서, 내부 슬롯(internal slot)과 내부 메서드(internal method)의 개념을 알아보자.

내부 슬롯과 내부 메서드는 자바스크립트 엔진의 구현 알고리즘을 설명하기 위해 EMCAScript 사양에서 사용하는 의사 프로퍼티와 의사 메서드이다. [[...]] 처럼 이중 대괄호로 감싸인 이름들이다.

하지만, 내부 슬롯과 내부 메서드는 개발자들이 외부에서 직접 접근할 수 없다. (단, 일부는 간접적으로 접근할 수 있는 수단을 제공한다. 

```
const o = {}

// 간접 접근 가능
console.log(o.__proto__) //[Object: null prototype] {}

// 직접 접근 불가
console.log(o.[[Prototype]]) //SyntaxError: Unexpected token '['
```

 

※ 의사 : 가짜 라는 뜻으로 스케치나 복사본의 의미로 사용되는 것 같다. 예를 들어 의사 코드(pseudocode)는 사람이 읽기 위해서 알고리즘의 로직을 간략히 적은 것을 의미한다. (컴퓨터가 이해하기 위한 문법이나 정보가 없기 때문에 진짜가 아니라 가짜라 볼 수 있고, 상세 알고리즘을 구현하기 위한 스케치 역할을 수행한다.)

 

### **프로퍼티 어트리뷰트와 프로퍼티 디스크립터 객체**

**자바스크립트 엔진은 프로퍼티를 생성할 때 프로퍼티의 상태를 나타내는 프로퍼티 어트리뷰트를 기본값으로 자동 정의한다.** 

프로퍼티의 상태란 프로퍼티의 값(value), 값의 갱신 여부(writable), 열거 가능 여부(enumerable), 재정의 가능 여부(configurable)를 말한다.

프로퍼티 어트리뷰트란 자바스크립트 엔진이 관리하는 내부 상태 값(meta-property)인 내부 슬롯 [[Value]]. [Writable]], [[Enumerable]], [[Configurable]]이다. 

 

이런 프로퍼티를 직접 접근을 불가능하지만, Object.getOwnPropertyDescriptor 메서드를 사용하여 간접적으로 확인은 가능하다.

```
const person = {
        name : 'lee'
}

console.log(Object.getOwnPropertyDescriptor(person, 'name')) 
// { value: 'lee', writable: true, enumerable: true, configurable: true }
```

위 메서드는 객체의 참조를 전달하고, 두 번째 매개변수는 프로퍼티의 키를 문자열로 전달한다. 이 때, 이 함수는 프로퍼티 디스크립터(Property Descriptor) 객체를 반환한다. 존재하지 않는 디스크립터를 요구하면 undefined가 반환된다.

 

### **데이터 프로퍼티와 접근자 프로퍼티**

프로퍼티는 데이터 프로퍼티와 접근자 프로퍼티로 나눌 수 있다.

데이터 프로퍼티는 키와 값으로 구성된 일반적인 프로퍼티로 우리가 여태까지 본 프로퍼티들이다.

\- value는 값을 저장,

\- writable은 수정권한으로 false면 수정이 불가능하여 읽기 전용인 된다.,

\- enumerable은 열거 권한으로 false면 Object.keys 등 열거 메서드를 사용 불가능하다.

\- configurable이 false면 프로퍼티의 삭제, 수정이 금지된다. (writable이 true면 값의 수정은 가능하다.)

 

접근자 프로퍼티는 자체적인 값을 갖지 않고 다른 데이터 프로퍼티의 값을 읽거나 저장할 때, 호출되는 접근자 함수(acccessor function)로 구성된 프로퍼티다.

\- get : gettter 함수가 호출되어 프로퍼티의 값이 반환된다.

\- set : setter 함수가 호출되어 프로퍼티의 값이 저장된다.

\- enumerable, configurable은 위와 동일한다.

해서, get,set을 getter ,setter 함수라 부르기도 한다.

```
const person = {
        firstName : 'hee',
        lastName : 'Lee',

    get fullName() {
            return `${this.firstName} ${this.lastName}`
    },
    //
    set fullName(name) {
            [this.firstName,this.lastName] = name.split(' ');
    }
}


console.log(person.firstName +' '+ person.lastName) // hee Lee
person.fullName = 'fiset last' // setter 함수가 자동으로 적용된다.
console.log(person.fullName) //first last, getter 함수가 자동으로 사용된다.
```

이 예시에서, 내부 슬롯/메서드 관점에서 설명하면 아래와 같다.

\1. 프로퍼티 키가 유효한지 확인한다. 키는 문자열 또는 심벌이어야만한다. (fullName은 문자열이므로 통과)

\2. 프로퍼티 체인에서 프로퍼티를 검색한다. (fullName은 존재)

\3. fullName이 데이터 프로퍼티인지 접근자 프로퍼티인지 확인한다. (여기서는 접근자 프로퍼티이다)

\4. 접근자 프로퍼티 fullName은 프로퍼티 어트리뷰트 [[Get]]의 값, 즉 getter 함수를 호출하여 그 결과를 반환한다.

 

※ 추가적으로, 왜 get,set 이름이 같은 지실험을 해보았는데 get/set은 같은 이름을 가져야 같은 접근자 프로퍼티에 배정된다.

```
const person = {
        firstName : 'hee',
        lastName : 'Lee',

    get fullName() {
            return `${this.firstName} ${this.lastName}`
    },
    set changefullName(name) {
            [this.firstName,this.lastName] = name.split(' ');
    }
}


person.fullName = 'first last' // 적용되지 않는다.
console.log(person.fullName) // hee Lee, 바뀌지 않은 값이 출력된다.

let descriptor = Object.getOwnPropertyDescriptor(person,'fullName')
descriptor.configurable = false
console.log(descriptor)

descriptor = Object.getOwnPropertyDescriptor(person,'changefullName')
console.log(descriptor)

// 출력결과
{
  get: [Function: get fullName],      
  set: undefined,
  enumerable: true,
  configurable: false
}
{
  get: undefined,
  set: [Function: set changefullName],
  enumerable: true,
  configurable: true
}
```

get, set을 이처럼 다르게 이름을 지으면 서로 다른 접근자 프로퍼티가 된다.



![img](https://blog.kakaocdn.net/dn/0Mnll/btsaESjnGl1/rsGJ33cTYwZm75o8S29kH1/img.png)webstorm에서는 set함수가 없으면 이를 read-only라고 한다.



 

※ 프로토타입은 어떤 객체의 상위 객체(부모) 역할을 하는 객체이다. 프로토타입은 하위 객체에게 자신의 프로퍼티와 메서드를 상속한다. 그래서 하위 객체느는 프로포타입의 메서드와 프로퍼티를 자유롭게 사용가능하다.

 

※ 프로토타입 체인은 프로트타입이 단방향 링크드 리스트 형태로 연결되어 있는 상속 구조를 말한다. 객체의 프로퍼티나 메서드에 접근할 때, 해당 객체에 접근 프로퍼티나 메서드가 없다면 프로토타입 체인을 따라서 상위 프로퍼티와 메서드를 검색한다.

 

### **프로퍼티 정의와 변경 방지**

object.defineProperty 메서드를 이용하면 프로퍼티를 정의할 수 있으며, 한 번에 여러개의 프로퍼티를 정의도 가능하다.

이 때, 생략한 값은 모두 false 또는 undefined가 된다.

 

이 때, 객체는 변경 가능한 값이므로 이를 금지하는 강도도 모두 다르다.



![img](https://blog.kakaocdn.net/dn/6aRQR/btsaEScCMUT/rPa2fgnktJN3dY3DWN1hsK/img.png)



```
const person = {
        name : 'hee',
}

Object.seal(person)
console.log(Object.isSealed((person))) // true

delete person.name // 밀봉되어서 삭제가 무시된다.
console.log(person) // { name: 'hee' }
```

이처럼 사용하면 된다.

하지만, 이는 얕은 변경 방지로 직속 프로퍼티만 적용되고, 하위에 존재하는 중첩 객체들은 영향을 주지 못한다. 따라서, 이를 완전한 불변객체로 쓰고싶다면, 재귀적으로 Object.freeze를 실행해야한다. 아래는 해당 코드이다

```
const person = {
    name : 'hee',
    address : {city : 'seoul'}
}
function deepFreeze(target) {
    if (target && typeof target === 'object' && !Object.isFrozen(target)) {
        Object.freeze(target)
        Object.keys(target).forEach(key => deepFreeze(target[key]))
    }
    return target
}

deepFreeze(person)

person.address.city = 'busan'
console.log(person) 

// 출력값
const person = {
    name : 'hee',
    address : {city : 'seoul'}
}
```

 

### **참고**

mdn, getOwnPropertyDescriptor : https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyDescriptor

 