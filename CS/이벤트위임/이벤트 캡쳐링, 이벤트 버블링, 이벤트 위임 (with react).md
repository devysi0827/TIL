# 이벤트 캡쳐링, 이벤트 버블링, 이벤트 위임 (with react)

### **이벤트 캡쳐링 / 버블링**

정의 : 

\- 이벤트 버블링 : 이벤트가 클릭한 하위요소에서 전파되어 부모까지 전달되는 현상

\- 이벤트 캡쳐링 : 이벤트가 클릭한 대상의 하위요소로 전파되는 현상, 기본적으로 off 상태로 사용되기 위해서 명시해야함



필요한 이유 : DOM의 특정 요소를 선택했을 때, 그 요소는 부모 내부에 있기에 이벤트를 상위와 하위로 전달하는 방법이 필요하다. 이 때, 사용되는 것이 이벤트 버블링과 캡쳐링이다.



이벤트 전파 순서 : (캡쳐링) -> 타겟 -> 버블링



### **캡쳐링과 버블링 중단**

하지만, 반대로 캡쳐링과 버블링으로 원하지 않는 요소에 이벤트가 전파되고 실행되어서 곤란할 수가 있다. 이를 해결위해서는 알맞게 이벤트를 전파하거나 이벤트의 흐름을 관리해야한다. 다음 요소들은 그를 위한 속성과 메서드들이다.



\- target : 처음 이벤트가 발생한 요소를 나타내는 속성

\- currentTarget : 이벤트를 처리하는 요소를 나태내는 속성

\- e.stopPropagation() : 버블링 또는 캡쳐링 전파를 중단시키는 메서드

\- e.stopImmediatePropagation() : 이벤트 전파 및 형제 이벤트 전파를 중단시키는 메서드

\- e.preventDefault() : 이벤트 전파 및 기본 이벤트 동작 자체를 차단한다.



### **이벤트 위임이란?**

정의

\- 특정 노드에 일일이 이벤트 리스너를 추가하는 대신, 이벤트 리스너를 특정 노드들을 포함하는 상위 노드에 연결하여 이벤트를 전파하는 것을 이벤트 위임이라고 합니다. 



원리

\- 이벤트 버블링과 캡쳐링 시, 부모 요소에게 전해지는 현상을 이용하여 상위 요소에서 하위 요소의 이벤트를 처리하는 것

장점
\- 동적 엘리먼트에 대한 이벤트 처리가 쉽다.
 \- 상위 엘리먼트에서 이벤트를 관리하기 때문에, 하위 엘리먼트를 자유롭게 추가 / 삭제할 수 있다.
\- 불필요한 메모리 낭비 최소화할 수 있다.
\- 관리가 유용하다.

단점
\- 이벤트 버블링을 막을 시, 에러가 날 수 있음
\- 반응하는 이벤트가 많아져서, CPU 부하를 증가시킬 수 있다



### 리액트에서의 이벤트 위임

![스크린샷 2024-11-09 오후 1.43.17](./이벤트 캡쳐링, 이벤트 버블링, 이벤트 위임 (with react).assets/스크린샷 2024-11-09 오후 1.43.17.png)

- 리액트는 동적인 컴포넌트 생성이 많이 있습니다. 관리와 메모리 절약 측면에서 상위에서 처리하도록 이벤트 위임을 사용합니다. 
  - 이미 이렇게 처리가 되어있기 때문에, React 사용자가 버블링을 사용하여도 메모리 상의 이점은 거의 존재하지 않습니다. (React 개발자 Dan 공식 답변)
- 본래 리액트는 document에 이벤트 위임을 진행하였으나, 여러 버전의 react가 충돌하는 문제가 발생하였습니다. 이는 예상치못한 버그를 만들 수 있기 때문에, document가 아닌 최상위 루트로 변경하도록 react 17에서 개선함.



### **참고자료**


React Github - issue 13635 : https://github.com/facebook/react/issues/13635?source=post_page-----b08f84e16250--------------------------------
React Legcy DOC - React 17 변경점 : https://legacy.reactjs.org/blog/2020/08/10/react-v17-rc.html#fixing-potential-issues

blog - event delegation test : https://dev.to/thawsitt/should-i-use-event-delegation-in-react-nl0

blog - 한눈에 이해하는 이벤트 흐름 제어 : [https://inpa.tistory.com/entry/JS-%F0%9F%93%9A-%EB%B2%84%EB%B8%94%EB%A7%81-%EC%BA%A1%EC%B3%90%EB%A7%81﻿](https://inpa.tistory.com/entry/JS-📚-버블링-캡쳐링)
