# React - Synchronizing with Effects

이 글은 리액트 공식문서를 개인적으로 해석 및 요약한 것입니다.  번역투를 해소하기 위해 약간의 수정을 추가하였습니다. 오역 등의 지적은 항상 환영합니다.

일부 전문 용어는 해석하지 않고 영문 단어를 그대로 적었으며, 첫 등장 시에만 ()를 이용하여 별도 표기하며 그대로 원문을 따라가기도 합니다.

원문 : https://react.dev/learn/synchronizing-with-effects

https://react.dev/reference/react/useEffect



# 들어가기에 앞서

"Effect"는 리액트에서 정의한 용어로, 렌더링에 의해서 발생하는 side effect를 의미합니다. 

Effect가 아닌 더 넓은 프로그래밍 개념으로의 side effect를 언급 시에는 side effect로 부를 것입니다.



# What are Effects and how are they different from events?

Effect를 알아보기 전에, 먼저 친숙한 두 가지 타입의 코드를 살펴보려합니다.

- Rendering code : (UI 설명에서 소개된) 렌더링 코드는 컴포넌트 최상위 수준에 있습니다. 이 코드는 state와 props를 가지고, 이를 전달하기도 하며, 화면에 jsx를 띄우는 역할을 합니다. 렌더링 코드는 수학 공식처럼 순수해야합니다. 렌더링코드는 결과만 계산해야하며, 다른 것은 하지 말아야합니다.
- Event Handlers : (Adding Interactivity에서 소개된) 이벤트 핸들러는 작업을 수행하는 컴포넌트 내부의 중첩함수로, 단순히 계산하는 것보다 더 나은 일을 수행합니다. 이벤트 핸들러는 입력 필드 업데이트, 물건을 사기 위한 HTTP POST  요청, 다른 화면으로 이동 등을 수행할 수 있습니다. 이벤트 핸들러는 프로그램의 상태를 변경하는 side effects를 포함하고 있습니다. 이 side effect는 유저의 행동(클릭, 입력)으로 인하여 발생합니다.



가끔씩은 위 두가지로는 충분하지 않습니다. 예시로, 채팅방을 고려해봅시다. 채팅방 컴포넌트는 스크린에 채팅이 보이는 한, 항상 채팅 서버와 연결되어 있어야합니다. 서버와 연결하는 것은 순수한 계산이 아니라 side effects이며, 그렇기 때문에 렌더링 중에는 일어날 수 없습니다. 그러나, 채팅을 보여주는 별도의 단일 이벤트(클릭과 같은)도 따로 없습니다.



Effects는 특정 이벤트가 아니라 렌더링 자체에 의한 side-effect를 지정할 수 있습니다. 메시지를 보내는 것은 사용자가 특정 버튼을 클릭하여서 나타나는 이벤트입니다. 그러나, 서버 연결을 설정하는 것은 Effects입니다. 왜냐하면, 컴포넌트와 상호작용 없이 발생하기 때문입니다. Effects는 화면 업데이트 후 커밋이 끝날 때 실행됩니다. 이것은 외부 시스템(네트워크, 라이브러리)들과 리액트 컴포넌트를 동기화하기에 아주 좋은 시기입니다.



# You might not need an Effect 

급하게 Effects를 컴포넌트에 추가하려 하지 마라.

Effects는 일반적으로 리액트 코드를 "빠져나오고(step out)" 외부 시스템과 동기화하는 데 사용한다. 

여기에는 browser APIs, third-party widgets, network 등등이 있다.

만약, Effect가 오직 다른 상태를 기준으로 한 일부 상태를 조정하는 정도라면 Effect는 불필요할 수도 있다.



# How to write an Effect 

이펙트를 쓰려면 다음 세 단계를 따라가라.



1. 이펙트를 선언해라 : 기본적으로 모든 이펙트는 렌더 이후 실행(run)됩니다.

2. 이펙트 종속성을 지정해라(specify the Effect dependecies) : 대부분의 이펙트는 모든 렌더 후가 아닌 필요할 때마다, 재실행(re-run)되어야합니다. 

예를 들면, 페이드인 애니메이션은 컴포넌트가 나타날때만 발동해야합니다. 채팅방의 연결과 연결 종료 또한, 채팅방 컴포넌트가 나타나고 사라질 때만 발생해야합니다.  당신은 이런 특정한 종속성을 제어하는 법을 배우게 될 것입니다.

3. 필요  시, 클린업을 추가해라(Add cleanup if needeed) : 몇몇 이펙트들은 언제 멈출 지를 지정해야합니다. 예를 들어서, connect-disconnect, subscribe-unsubcibe, fetch-cancle의 관계처럼말입니다. 당신은 클린업 함수를 이용하여 어떻게 멈출 지를 배우게됩니다.  



이제 각 단계를 상세히 말하고자 한다.



# Step 1: Declare an Effect 

