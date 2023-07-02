# Closure

### **클로져란?**

정의 : 함수와 렉시컬 환경의 조합. 흔히, 본인이 포함된 상위 함수보다 오래 살아있는 중첩함수를 의미하기도 한다.

이해를 위해 필요한 개념 :

- 스코프 체인 : 현재 위치에서 함수에 필요한 변수를 탐색을 하고, 없을 경우 스코프체인을 통해서 상위 함수에서 변수를 찾는다. 끝까지 찾지 못할 시, 참조 에러를 발생시킨다.
- 렉시컬 스코프(정적 스코프) : 함수가 생성(정의)될 당시의 상위 스코프와 그에 따른 외부 변수를 기억하고 생성 이후에도 계속 접근이 가능할 수 있게 하는 스코프 규칙이다. 생성 될 때를 기준으로 하기에, 상위 함수의 생명주기가 끝나도, 상위 함수의 변수의 접근이 가능하다.

- 자유 변수 : 생명 주기가 끝난 상위 함수의 변수를 자유 변수라 한다.
- 실행 컨텍스트 : javascript 코드를 실행하는 환경으로 코드 실행에 필요한 변수, 함수 , 매개변수 등의 정보를 담고 있다. 스택 구조로, 맨 위에 있는 실행 컨텍스트가 현재 실행중인 코드의 제어권을 가지고 있다.
- 렉시컬 환경 : 실제 데이터 구조로 식별자와 해당 식별자의 값을 연결하는 데이터 자료구조이다. 실행 컨텍스트들은 각각 이 환경을 가진다 생각해도 된다.

※ 동적 스코프 : 함수 호출 위치에 따라 상위 스코프를 결정한다. js와 관계없지만, 참고사항으로 적어둔다.



### **클로져의 동작과정**

![img](https://blog.kakaocdn.net/dn/FfGIE/btslRQ39qan/SgzHax2MokFyPQfqZ1h2r1/img.png)

10분 테크톡의 엘라님의 자료이다. 이 분의 설명이 굉장히 깔끔해서 이를 사용하기로 했다.

ella()를 실행시키면 1이 아니라 10이 나오는 이유는 클로져때문이다. 그 원리를 더 자세하게 보자.



![img](https://blog.kakaocdn.net/dn/B3SeL/btslRnBdkFD/6DAVLmd7E0uiKAwOlW4gwk/img.png)

이처럼 실행 컨텍스트에서 특정 함수를 실행 시킬 때, 해당 함수와 관련된 렉시컬 환경을 확인하게 된다.

ella는 inner 함수를 가리키고 inner함수는 내부 슬롯을 통해 본인의 렉시컬 환경을 확인한다. 이 때, x라는 변수가 렉시컬 환경에 존재하므로 x = 10이 출력된다.



### **클로져는 그럼 어디서 사용될까?**

위 예시도 있지만, 클로져는 생각보다 우리가 많이 사용한다.

대표적인 예는 css입니다. 본인 태그나 아이디에 더 알맞는 변수가 있다면, 그 부분을 적용합니다. 없다면, 상위 스코프로 이동하여 부모의 스타일을 따라갑니다.

```
body {
  font-family: Helvetica, Arial, sans-serif;
  font-size: 12px;
}

h1 {
  font-size: 1.5em;
}

h2 {
  font-size: 1.2em;
}
```

또한, 아래와 같은 버그들도 있을 것입니다.

```
function showHelp(help) {
  document.getElementById("help").textContent = help;
}

function setupHelp() {
  var helpText = [
    { id: "email", help: "Your email address" },
    { id: "name", help: "Your full name" },
    { id: "age", help: "Your age (you must be over 16)" },
  ];

  for (var i = 0; i < helpText.length; i++) {
    // Culprit is the use of `var` on this line
    var item = helpText[i];
    document.getElementById(item.id).onfocus = function () {
      showHelp(item.help);
    };
  }
}

setupHelp();
```

[Demo1](https://jsfiddle.net/v7gjv/8164/)

![img](https://blog.kakaocdn.net/dn/crGdw1/btslRILI91j/uFobQECgfT9tsswxM68cjk/img.png)

```
function showHelp(help) {
  document.getElementById('help').innerHTML = help;
}

function makeHelpCallback(help) {
  return function() {
    showHelp(help);
  };
}

function setupHelp() {
  var helpText = [
      {'id': 'email', 'help': 'Your e-mail address'},
      {'id': 'name', 'help': 'Your full name'},
      {'id': 'age', 'help': 'Your age (you must be over 16)'}
    ];

  for (var i = 0; i < helpText.length; i++) {
    var item = helpText[i];
    document.getElementById(item.id).onfocus =
       makeHelpCallback(item.help);
  }
}

setupHelp();
```

[Demo2](https://jsfiddle.net/v7gjv/9573/)

![img](https://blog.kakaocdn.net/dn/c4AVPw/btslRSnqfpO/TxS8X32WvUYXOec9C24mik/img.png)



Demo1은 동작이 제대로 되지 않지만, Demo2의 경우 정상적으로 작동함을 볼 수 있습니다.

두 코드의 차이점이 발생하는 이유는 Demo1은 함수 스코프를 공유하고 있어서, 결국 마지막 help값을 모든 곳에서 동일하게 사용하지만, Demo2는 함수 스코프가 각각 별도이므로, focus 될 때 해당 값이 나타나는 것입니다. 

이런 식으로 클로져를 제대로 이해하지 못했다면, 예상치못한 버그가 발생할 수 있습니다.

 

### **참고자료**

mdn : https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures

배민 테크톡(closure) : https://www.youtube.com/watch?v=PVYjfrgZhtU&t=233s