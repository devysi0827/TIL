# **모던 자바스크립트 Deep Dive 2장 : 자바스크립트란?**



 

## **표준화된 자바스크립트 (ECMA)의 변화과정**

1995년 : 웹페이지의 보조적인 기능 수행을 위해서 브라우저에서 동작하는 경량 프로그래밍 언어(JS 초기 버전) 도입

1996년 : 브라우저 간 경쟁으로 크로스 브라우징 이슈 발생. 표준화된 언어 개발 착수

1997년 : ECMA-262 표준화된 자바스크립트 초판(ECMAScript1) 발행

2009년 : ECMASciprt5(ES5)가 HTML5와 함께 출시

2015년 : ECMASciprt6(ES6)가 let/const 키워드, 화살표 함수, 클래스, 모듈 등과 같은 범용 프로그래밍 언어로서 갖춰야할 대규모 기능이 도입

2015~ : 지속적으로 매년 소규모 업데이트 진행 



## **성장의 역사**

#### 시작 (1995년)

\- HTML +CSS를 서버로부터 받아서 렌더링하는 도구

#### AJAX 출현 (1999년)

\- JavaSciprt를 이용하여 비동기방식으로 데이터를 교환할 수 있는 통신이 가능한 AJAX가 출현.

\- before : 기존은 HTML에서 한 부분이라도 변경해야할 시, 모든 HTML 코드를 서버로부터 다시 받아서 재렌더링 진행 =>느리고 화면 전체가 깜박거림

\- after : 서버로부터 필요한 부분만데이터를 받아서 변경 => 빠르고 부드러운 화면 전환이 가능해짐

#### jQuery의 출현 (2006년)

\- 이전까지 논란이 있었던 DOM 제어와 크로스 브라우징 이슈를 해결

\- 직관적인 사용법의 사용자가 활성화

#### V8 JS 엔진 (2008년)

\- 웹 애플리케이션 프로그래밍 언어로서 활성화되기 위해서 이를 더욱 빠르게 동작하려는 자바스크립트 엔진을 필요로 함.

\- Google에서 V8 JS 엔진을 개발하고 이는 요구에 맞는 성능을 제공

\- 웹 개발 -> 프런트 개발로 바뀌는 시발점이 됨

#### Node.js

\- V8을 기반으로한 JS 런타임 환경이다.

\- 브라우저 외에도 사용가능하며, 필요한 모듈, 파일 시스템, HTTP 등 빌트인 API를 제공한다.

\- Node.js에 출현으로 서버 개발도 가능한 범용 프로그래밍 언어로 자리잡았다.

\- 비동기 I/O를 지원하며, 단일 스레드 이벤트 루프 기반으로 동작하여 요청 처리 성능이 더 좋다. 그래서, 데이터 실시간 처리가 많은 SPA등에는 적합하나 CPU 사용률이 높은 애플리케이션에는 권장하지 않는다.
=> 단일 스레드이기 때문에, CPU 사용률이 높은 애플리케이션을 사용하면 딜레이 관련 문제가 생길 수 있다.
=> 다음 유튜브 영상을 보면 좋을 거 같다.

https://www.youtube.com/watch?time_continue=999&v=ZeRJycLzh1g&embeds_euri=https%3A%2F%2Fdevysi0827.tistory.com%2F44&feature=emb_logo



###  SPA 프레임워크

\- 개발 규모와 복잡도가 상승함에 따라서, 많은 패턴과 라이브러리가 출현했다.



## **자바스크립트와 ECMAScript**

\- JavaScript = ECMAScript(표준화된 js) + 브라우저(클라이언트 사이드) Web API

\- 그래서 각 브라우저별로 제공하는 Web API에 따라서, 성능과 최적화 그리고 기능등이 달라지게 되는 이슈가 있다.(크로스 브라우징 이슈)

\- ECMAScript는 ECMA에서, Web API는 W3C에서 관리하고 있다.



## **자바스크립트 특징**

\- 인터프리터 언어, 하지만 인터프리터의 단점인 실행 속도를 일부 소소코드만 컴파일학 실행하는 방법으로 극복했다.

\- 명령형, 함수형, 프로토타입 기반 객체지향 프로그래밍을 지원하는 멀티 패러다임 프로그래밍 언어이다.(클래스 기반이 아니여서 객체지향이 아니라 오해받으나, 충분히 객체지향이다)



## **키워드 / 참고자료**

렌더링 : HTML + CSS +JS로 작성된 문서를 해석해서 브라우저에 시각적으로 출력하는 것

서버사이드렌더링(SSR) : 서버에서 데이터를 HTML로 변환해서 전달하는 것

크로스 플랫폼 : 크로스 플랫폼 또는 멀티 플랫폼은 컴퓨터 프로그램, 운영 체제, 컴퓨터 언어, 프로그래밍 언어, 컴퓨터 소프트웨어 등이 여러 종류의 컴퓨터 플랫폼에서 동작할 수 있다는 것을 뜻하는 용어



크로스 브라우징 이슈 : 브라우저마다 제공하는 성능과 방식이 달라서 브라우저마다 최적화나 정보량이 달라지는 현상.

[
크로스 브라우징이란?'크로스 브라우징' 이라는 용어가 나온지도 10년이 훌쩍 넘은 듯 하다. 그런데 10년이 넘도록 크로스 브라우징에 대한 이해는 여전히 잘못된 면모가 자꾸 보인다.mulder21c.github.io](https://mulder21c.github.io/2019/01/30/what-is-cross-browsing/)



[
Introduction to cross-browser testing - Learn web development | MDNThis article should have given you a high-level understanding of the most important concepts you need to know about cross browser testing. Armed with this knowledge, you are now ready to move on and start learning about Cross browser testing strategies.developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Cross_browser_testing/Introduction)



Node와 이벤트 루프

[
Node.js 이벤트 루프, 타이머, `process.nextTick()` | Node.jsNode.js® is a JavaScript runtime built on Chrome's V8 JavaScript engine.nodejs.org](https://nodejs.org/ko/docs/guides/event-loop-timers-and-nexttick)



JS와 ES의 차이는?

[
JavaScript와 ECMAScript는 무슨 차이점이 있을까? - 재그지그의 개발 블로그웹 개발에서 JavaScript와 ECMAScript라는 용어가 혼용되어 사용되고 있는 이유와 그 차이점에 대해 알아봅니다.wormwlrm.github.io](https://wormwlrm.github.io/2018/10/03/What-is-the-difference-between-javascript-and-ecmascript.html)



[
What’s the difference between JavaScript and ECMAScript?by Michael Aranda What’s the difference between JavaScript and ECMAScript? I’ve tried googling “the difference between JavaScript and ECMAScript.” I ended up having to wade through a sea of ambiguous and seemingly conflicting results: “ECMAScriptwww.freecodecamp.org](https://www.freecodecamp.org/news/whats-the-difference-between-javascript-and-ecmascript-cba48c73a2b5)



프로토타입 객체지향

[
상속과 프로토타입 - JavaScript | MDNJava 나 C++ 같이 클래스 기반의 언어를 사용하던 프로그래머는 자바스크립트가 동적인 언어라는 점과 클래스가 없다는 것에서 혼란스러워 한다. (ES2015부터 class 키워드를 지원하기 시작했으나,developer.mozilla.org](https://developer.mozilla.org/ko/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)



[
프로토타입 기반 프로그래밍 - 위키백과, 우리 모두의 백과사전위키백과, 우리 모두의 백과사전. 프로토타입 기반 프로그래밍은 객체지향 프로그래밍의 한 형태의 갈래로 클래스가 없고, 클래스 기반 언어에서 상속을 사용하는 것과는 다르게, 객체를 원형(ko.wikipedia.org](https://ko.wikipedia.org/wiki/프로토타입_기반_프로그래밍)