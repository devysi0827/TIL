# React의 기본 원리

React 철학

React fiber

React portal

React 18,19 변경점

ref = native dom을 조작함.



shouldComponentUpdate

hydrateRoot



[기초 - 생략 가능]

- 리액트는 라이브러리인가요 프레임워크 인가요?🔥

  - A. 라이브러리

- 리액트를 사용하는 이유🔥🔥

  - A. 개발 생산성을 높이기 위해서

- props와 state의 차이🔥

  - props : 컴포넌트에 데이터를 전달해줌. 컴포넌트에서 변경이 되지 않음
  - state : 컴포넌트 내부에서 관리하는 데이터

- Props가 컴포넌트간에 전달받는 것이라고 했는데 자식에서 부모로도 전달할 수 있는가 🔥

  - A. 불가능. 단, 자식에서 props를 변화시키는 함수를 전달받을 수는 있음

- FLUX에 대해서 아나요? 🔥🔥

  - A. 데이터를 단방향으로 흐르게 하는 아키텍처 패턴
  - Action(상태 변경 트리거) - Dispatcher(내용 전달) - Store(데이터 변경) - View(렌더링) 형식으로 진행함

  

[React VDOM + 렌더링 + Fiber]

- virtual DOM에 대해서 아나요?🔥🔥
  - A. 가상의 돔으로, dom을 업데이트하고 
  - DOM 변경은 비용이 많이 들기 때문에, 가상의 DOM을 생성하고 가상 DOM의 변경사항만을 추적하여 실제 DOM에 적용하는 방식은 빠르고 비용이 적게듬
    - svelte : VDom의 비교 연산이 공짜가 아니기 때문에, 컴파일 단계에서 이를 계산하고 바로 반영하여 최적화함
    - vdom은 메모리에서만 존재하며 dom의 가벼운 복사본으로 성능에는 큰 문제가 없음. 다만, 비교 및 적용 부분에서는 약간의 오버헤드가 있을 수 있음
- 리액트의 렌더링에 대해 아나요?
  - 상태 변화 -> VDOM 반영 -> diffing -> dom 업데이트 -> 렌더링
  - batching, useMemo,useCallback 등으로 렌더링 최적화 
  - key가 동일 할 때, 렌더링을 생략함

- 리액트 파이버에 대해서 아나요?
  - 리액트가 vdom을 활용하여 증분 렌더링을 적용 하는 재조정 엔징입니다.
- 리액트 파이버 트리
  - 
- 리액트 파이버와 DOM, Virtual DOM의 관계
  - 
- 렌더 단계와 커밋 단계에 대해 아나요?
  - Render 단계: JSX 선언 또는 `React.createElement()`를 통해 일반 객체인 Reat 엘리먼트를 생성한다.
  - Reconcile 단계: 이전에 렌더링된 실제 DOM 트리와 새로 렌더링할 React 엘리먼트를 비교하여 변경점을 적용한다.
  - Commit 단계: 새로운 DOM 엘리먼트를 브라우저 뷰에 커밋한다.
  - Update 단계: props, state 변경 시 해당 컴포넌트와 하위 컴포넌트에 대해 위 과정을 반복한다.



[React 클래스 vs 함수형]

- ~~React에서 함수 컴포넌트와 클래스 컴포넌트의 차이 🔥~~
  - 
- 리액트에서 함수형 컴포넌트라고 부르지 않고 함수 컴포넌트라고 부르는 이유가 무엇인가요 🔥
  - 



[Redux]

- 리덕스에 대해서 아나요? 🔥🔥
- 리덕스의 기본 원칙은? 🔥🔥



[불변성]

- React에서 state의 불변성을 유지하라는 말이 있는데 이에 대해 설명해달라 🔥
- 리듀서 내부에서 불변성을 지키는 이유는? 전개 연산자의 단점을 해결할 수 있는 방법은 무엇인가



# 참고문서

svelet - [better vdom](https://svelte.dev/blog/virtual-dom-is-pure-overhead)

naverD2 - [fiber 분석 ](https://d2.naver.com/helloworld/2690975)