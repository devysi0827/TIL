# React Virtual DOM and Reconciliation

### DOM

- 정의 : 문서 객체 모델(The Document Object Model, 이하 DOM) 은 HTML, XML 문서의 프로그래밍 interface 이다.

- 용도 : DOM은 문서의 구조화된 표현(structured representation)을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공하여 그들이 문서 구조, 스타일, 내용 등을 변경할 수 있게 돕는다.

- 구조 : nodes와 objects로 구성된다. 

- 발전사항 : 초창기 DOM은 JS와 밀접하게 연관되어 있었지만 지금은 분리해서 각각 발전되었다. 따라서 페이지 콘텐츠들은 DOM에 저장되고 이를 JS로 접근 및 조작하는 방식이 대표적이다.

  `API (web or XML page) = DOM + JS (scripting language)`

  



### Virtual DOM

- 정의 : UI의 가상적인 표현을 메모리에 저장하고 실제 DOM과 동기화하는 프로그래밍 개념입니다.
- 이 때, 동기화를 위하여 비교하는 과정을 `재조정(Reconciliation)`이라 한다.









### 참고문서

https://velog.io/@syoung125/eact-Reconciliation%EC%9D%B4%EB%9E%80-virtual-DOM-%EB%A6%AC%EC%95%A1%ED%8A%B8%EA%B0%80-%EC%84%A0%EC%96%B8%EC%A0%81

https://ko.reactjs.org/docs/reconciliation.html

https://brunch.co.kr/@eight-two-five/14

https://programmingwithmosh.com/react/react-virtual-dom-explained/

https://ui.toast.com/weekly-pick/ko_20210819



MDN 공식문서 DOM : https://developer.mozilla.org/ko/docs/Web/API/Document_Object_Model/Introduction

React 공식문서 (Virtual DOM) : https://ko.reactjs.org/docs/faq-internals.html#what-is-the-virtual-dom