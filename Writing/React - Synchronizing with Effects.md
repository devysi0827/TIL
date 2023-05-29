# React - Synchronizing with Effects

이 글은 리액트 공식문서를 개인적으로 해석 및 요약한 것입니다.  

- 번역투를 해소하기 위해 약간의 수정이 있습니다.

- 오역이나 설명이 부족한 부분에 대한 설명은 항상 환영합니다.

- 일부 전문 용어는 해석하지 않고 영문 단어를 그대로 적었으며, 첫 등장 시에만 ()를 이용하여 별도 표기하며 그대로 원문을 따라가기도 합니다.

원문 : https://react.dev/learn/synchronizing-with-effects

참고 : https://react.dev/reference/react/useEffect



# 들어가기에 앞서

"Effect"는 리액트에서 정의한 용어로, 렌더링에 의해서 발생하는 side effect를 의미합니다. 

Effect가 아닌 더 넓은 프로그래밍 개념으로의 side effect를 언급 시에는 side effect로 별도 부를 것입니다.



# What are Effects and how are they different from events?

Effect를 알아보기 전에, 먼저 친숙한 두 가지 타입의 코드를 살펴보려합니다.

- Rendering code : (UI 설명에서 소개된) 렌더링 코드는 컴포넌트 최상위 수준에 있습니다. 이 코드는 state와 props를 가지고, 이를 전달하기도 하며, 화면에 jsx를 띄우는 역할을 합니다. 렌더링 코드는 수학 공식처럼 순수해야합니다. 렌더링코드는 결과만 계산해야하며, 다른 것은 하지 말아야합니다.
- Event Handlers : (Adding Interactivity에서 소개된) 이벤트 핸들러는 작업을 수행하는 컴포넌트 내부의 중첩함수로, 단순히 계산하는 것보다 더 나은 일을 수행합니다. 이벤트 핸들러는 입력 필드 업데이트, 물건을 사기 위한 HTTP POST  요청, 다른 화면으로 이동 등을 수행할 수 있습니다. 이벤트 핸들러는 프로그램의 상태를 변경하는 side effects를 포함하고 있습니다. 이 side effect는 유저의 행동(클릭, 입력)으로 인하여 발생합니다.



가끔씩은 위 두가지로는 충분하지 않습니다. 

예시로, 채팅방을 고려해봅시다. 채팅방 컴포넌트는 스크린에 채팅이 보이는 한, 항상 채팅 서버와 연결되어 있어야합니다. 서버와 연결하는 것은 순수한 계산이 아니라 side effects이며, 그렇기 때문에 렌더링 중에는 일어날 수 없습니다. 그러나, 채팅을 보여주는 별도의 단일 이벤트(클릭 등)도 따로 없습니다.



Effects는 특정 이벤트가 아니라 렌더링 자체에 의한 side effect를 지정할 수 있습니다. 메시지를 보내는 것은 사용자가 특정 버튼을 클릭하여서 나타나는 이벤트입니다. 그러나, 서버 연결을 설정하는 것은 Effects입니다. 왜냐하면, 컴포넌트와 상호작용 없이 발생하기 때문입니다. Effects는 화면 업데이트 후 커밋이 끝날 때 실행됩니다. 이것은 외부 시스템(네트워크, 라이브러리)들과 리액트 컴포넌트를 동기화하기에 아주 좋은 시기입니다.



# You might not need an Effect 

급하게 Effects를 컴포넌트에 추가하려 하지 맙시다.

Effects는 일반적으로 리액트 코드를 **빠져나오고(step out)** 외부 시스템과 동기화하는 데 사용합니다. 

예시로, browser APIs, third-party widgets, network 등이 있습니다.

만약, Effect가 오직 다른 상태를 기준으로 한 일부 상태를 조정하는 정도라면 Effect는 불필요할 수도 있습니다.



# How to write an Effect 

이펙트를 쓰려면 다음 세 단계를 따라가라.



1. 이펙트를 선언해라 : 기본적으로 모든 이펙트는 렌더 이후 실행(run)됩니다.

2. 이펙트 종속성을 지정해라(specify the Effect dependecies) : 대부분의 이펙트는 모든 렌더 후가 아닌 필요할 때마다, 재실행(re-run)되어야합니다. 

예를 들면, 페이드인 애니메이션은 컴포넌트가 나타날때만 발동해야합니다. 채팅방의 연결과 연결 종료 또한, 채팅방 컴포넌트가 나타나고 사라질 때만 발생해야합니다.  당신은 이런 특정한 종속성을 제어하는 법을 배우게 될 것입니다.

3. 필요  시, 클린업을 추가해라(Add cleanup if needeed) : 몇몇 이펙트들은 언제 멈출 지를 지정해야합니다. 예를 들어서, connect-disconnect, subscribe-unsubcibe, fetch-cancle의 관계처럼말입니다. 당신은 클린업 함수를 이용하여 어떻게 멈출 지를 배우게됩니다.  



이제 각 단계를 상세히 설명해보겠습니다.



# Step 1: Declare an Effect 

 useEffect Hook을 불러온다.

```
import { useEffect } from 'react';
```



그리고 컴포넌트 최상단에 useEffect를 호출하고, 그 안에 Effect code를 작성힌디/

```
function MyComponent() {
  useEffect(() => {
    // Code here will run after *every* render
  });
  return <div />;
}
```



컴포넌트가 렌더링 될 때마다, 리액트는 화면을 업데이트하고 `useEffect`내부에 코드를 실행할 것입니다. 즉, `useEffect`는 렌더가 화면에 반영될 때까지 코드 조각이 실행되지 않도록 **지연**합니다.



이제, Effect가 외부시스템과 어떻게 동기화되는 지 살펴보겠습니다. <VideoPlayer> React 컴포넌트를 예시로 보겠습니다. 이 컴포넌트는 isPlaying이라는 props에 따라서 정지와 재생을 제어할 수 있습니다.

```
<VideoPlayer isPlaying={isPlaying} />;
```



우리가 만든 커스텀 `videoPlayer` 컴포넌트는 내장된 video tag를 렌더할 것입니다.

```
function VideoPlayer({ src, isPlaying }) {
  // TODO: do something with isPlaying
  return <video src={src} />;
}
```

그러나, 내장된 video tag는 isPlaying이란 prop이 없습니다. 유일하게 video를 컨트롤하는 방법은 DOM element에서 play()와 pause()를 호출하는 것입니다. 

당신은 Playing prop의 값과 play(), pasue() 의 호출을 동기화해야합니다. 



먼저, 우리는 video DOM node에 참조를 걸어야합니다. 

렌더링 도중에 play() 나 pause()를 호출하려고 할 수 있지만, 이는 올바르지 않습니다.

```
// 여기서는 간략화된 코드만을 기술합니다. 전체 코드를 보고 싶다면, 원문을 참고하길 바랍니다.
function VideoPlayer({ src, isPlaying }) {
  const ref = useRef(null);

  if (isPlaying) {
    ref.current.play();  // Calling these while rendering isn't allowed.
  } else {
    ref.current.pause(); // Also, this crashes.
  }

  return <video ref={ref} src={src} loop playsInline />;
}
```

아래 코드는 에러가 발생하게됩니다.

이 코드가 올바르지 않은 이유는 렌더링 중에 DOM 노드로 작업을 시도하기 때문입니다. 리액트에서, 렌더링은 JSX의 순수한 계산이어야만 합니다. DOM 수정과 같은 side effect를 포함하면 안됩니다.

추가로, videoPlayer를 첫 번째로 호출하였을 때, DOM은 아직 존재하지 않습니다. 그래서 DOM의 play() 와 pause()를 호출할 수 없습니다. 왜냐하면, JSX가 반환하기 전까지 React는 어떤 DOM이 만들어지는 지 알 수 없기 때문입니다.

```
function VideoPlayer({ src, isPlaying }) {
  const ref = useRef(null);

  useEffect(() => {
    if (isPlaying) {
      ref.current.play();
    } else {
      ref.current.pause();
    }
  });

  return <video ref={ref} src={src} loop playsInline />;
}
```



이 문제에 대한 해결책은 side effect를 useEffect로 감싸서 렌더링 계산에서 제외시키는 것입니다.

이렇게 진행될 경우, 렌더링이 된 후, Effect가 실행됩니다.

<videoPlayer>가 렌더 되었을 때 아래와 같은 일들이 일어납니다.

먼저, 리액트가 화면에 업데이트를 하고 <video> tag가 DOM에 올바르게 있는 지 확인합니다. 그 후, 리액트는 Effect를 실행합니다. 마지막으로. Effect는 `isPlaying`변수 값에 따라서 play() 나 pause()를 호출합니다. 



이 예제는 브라우저 미디어 API라는 외부시스템과  React 상태를 동기화한 예시입니다. 유사한 방법으로 legacy non React code(jQuery plugin) 등을 선언현 React Components로 래핑할 수 있습니다.



실제 비디오 플레이어 제어는 훨씬 더 복잡합니다. 이 예제는 매우 단순한고 불완전한 예시임을 참고 바랍니다.



### 주의

기본적으로, Effects는 매 렌더마다 실행됩니다. 그래서 아래 코드는 무한루프가 진행됩니다.

```
const [count, setCount] = useState(0);
useEffect(() => {
  setCount(count + 1);
});
```

Effects는 렌더링의 결과로 실행됩니다. 상태를 세팅하는 것은 렌더링을 유발합니다. Effect에서 상태를 세팅하는 전자제품의 콘센트에 자신의 플러그를 꽃는 것과 비슷합니다. 이펙트가 실행되면서 상태가 세팅되고, 이것은 리렌더를 유발합니다. 그리고 이 리렌더는 다시 이펙트를 실행시킵니다. 그리고 계속 무한히 반복됩니다...



이펙트는 주로 외부시스템과 동기화를 위하여 사용해야한다. 만약, 외부시스템이 없고 오직 상태를 조정하기 위해서라면 이펙트가 필요없을 것이다.



# Step 2: Specify the Effect dependencies 

기본적으로, 이펙트는 매 렌더마다 실행된다. 하지만 이것은 당신이 원하는 바가 아닐것이다.

- 가끔씩은 이것은 느리다. 항상 실시간으로 외부와 동기화될 필요는 없고 생략하길 바랄 것이다. 예를 들면, 우리가 타자를 칠 때마다 채팅서버를 다시 연결할 필요는 없지 않은가
- 가끔씩은 이것은 틀리다. 예를 들면, 페이드인은 한번만 실행되면 된다. 매 타이핑마다 페이드인이 실행되기 바라지는 않을 것이다.

이것을 증명하기 위해서, 예시를 준비하였다. input에 타이핑을 해보면, 이펙트가 재실행되는 것을 볼 수 있다.

```
function VideoPlayer({ src, isPlaying }) {
  const ref = useRef(null);

  useEffect(() => {
    if (isPlaying) {
      console.log('Calling video.play()');
      ref.current.play();
    } else {
      console.log('Calling video.pause()');
      ref.current.pause();
    }
  });

  return <video ref={ref} src={src} loop playsInline />;
}

export default function App() {
  const [isPlaying, setIsPlaying] = useState(false);
  const [text, setText] = useState('');
  return (
    <>
      <input value={text} onChange={e => setText(e.target.value)} />
      <button onClick={() => setIsPlaying(!isPlaying)}>
        {isPlaying ? 'Pause' : 'Play'}
      </button>
      <VideoPlayer
        isPlaying={isPlaying}
        src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"
      />
    </>
  );
}
```

사진 첨부

의존성 배열을 특정함으로서 리액트가 이런 불필요한 재실행을 스킵할 수 있다. 

```
  useEffect(() => {
    // ...
  }, []);
```

다만, 위 예시에서는 `React Hook useEffect has a missing dependency: 'isPlaying'` 이라는 에러를 볼 수 있다.

이 문제는  Effect 내부의 코드가 `isPlaying` prop에 의해서 무엇을 할지 결정되기 때문이다. 하지만, 이 의존성은 명확하게 선언되지 않았다. 이 문제를 해결하기 위해서, 의존성 배열에 isPlaying을 추가하자

```
  useEffect(() => {
    if (isPlaying) { // It's used here...
      // ...
    } else {
      // ...
    }
  }, [isPlaying]); // ...so it must be declared here!
```

이제 모든 의존성배열은 선언되었고, 에러가 없다. 의존성 배열에 isPlaying 변수를 특정함으로서, 리액트에게 만약, 'isPlaying' 변수가 동일하다면, 해당 이펙트를 스킵하라 전달할 수 있게된다.

이런 설정과 함께라면, 위에 타이핑은 더 이상 리렌더를 발생시키지 않는다.

```
import { useState, useRef, useEffect } from 'react';

function VideoPlayer({ src, isPlaying }) {
  const ref = useRef(null);

  useEffect(() => {
    if (isPlaying) {
      console.log('Calling video.play()');
      ref.current.play();
    } else {
      console.log('Calling video.pause()');
      ref.current.pause();
    }
  }, [isPlaying]);

  return <video ref={ref} src={src} loop playsInline />;
}

export default function App() {
  const [isPlaying, setIsPlaying] = useState(false);
  const [text, setText] = useState('');
  return (
    <>
      <input value={text} onChange={e => setText(e.target.value)} />
      <button onClick={() => setIsPlaying(!isPlaying)}>
        {isPlaying ? 'Pause' : 'Play'}
      </button>
      <VideoPlayer
        isPlaying={isPlaying}
        src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"
      />
    </>
  );
}

```

의존성 배열은 여러 의존성을 담을 수 있고, 리액트는 이 의존성 배열이 모두 이전 렌더링과 동일한 값을 가질때만 스킵을 진행합니다. 리액트는 object.is 비교를 통해서 의존성배열을 비교합니다. 자세한 것은 useEffect 문서를 참고 바랍니다.



주의할 것은 당신은 당신의 의존성을 **선택할 수 없습니다.** 리액트가 예상하는 Effect의 의존성배열과 동일하지 않으면 lint 에러가 발생할 것입니다. 이것은 수많은 버그를 고치는 데 도움을 줄 것입니다. 만약, 당신이 코드를 재실행하기 원하지 않는다면, Effect code 자체에 의존성이 없도록 작성하십쇼



### 주의

비어있는 의존성 배열과 없는 의존성 배열은 행동이 다릅니다.

```
useEffect(() => {
  // This runs after every render
});

useEffect(() => {
  // This runs only on mount (when the component appears)
}, []);

useEffect(() => {
  // This runs on mount *and also* if either a or b have changed since the last render
}, [a, b]);
```



### Why was the ref omitted from the dependency array?

이펙트는 'ref'와 isPlaying 두 변수를 사용합니다. 하지만, isPlaying만 존재하는 이유는 무엇일가요?

왜냐하면, ref 객체는 안정적인 정체성을 가지기 때문입니다. 리액트는 매 렌더마다 당신이 useRef로부터 항상 같은 객체를 갖도록 보증해줍니다. 그래서 이것은 변하지 않으며, 리렌더를 유발하지 않습니다. 그러므로 ref는 있든 없든 아무런 영향을 주지 않습니다.

set 함수도 안정적인 정체성을 갖기때문에 의존성배열에서 누락될 수 있습니다. 린트도 이를 허용해줍니다.

이런 누락은 린트가 확인했을 때, 의존성이 항상 안정적이라 판단되면 작동합니다.



# Step 3: Add cleanup if needed 

다른 예시를 살펴봅시다.

당신은 챗룸 컴포넌트를 제작중이고, 이 컴포넌트가 나타낼 때 서버가 연결되어야합니다.

당신은 connect()와 disconnect() 메서드를 반환하는 crateConnection API를 가지고 있습니다.

당신은 어떻게 컴포넌트 나타낼 때, 이 연결을 유지하겠습니까?



시작은 아래처럼 해봅시다.

```
useEffect(() => {
  const connection = createConnection();
  connection.connect();
});
```

이 코드는 매 렌더마다 리렌더를 하기에 느립니다. 의존성 배열을 추가해줍시다.

```
useEffect(() => {
  const connection = createConnection();
  connection.connect();
}, []);
```

이렇게 빈 배열은 가진 코드는 컴포넌트가 마운트될 때 단 한번만 실행됩니다.

```
import { useEffect } from 'react';
import { createConnection } from './chat.js';

export default function ChatRoom() {
  useEffect(() => {
    const connection = createConnection();
    connection.connect();
  }, []);
  return <h1>Welcome to the chat!</h1>;
}
```

하지만, 이 코드를 실행하니 로그가 두 개가 생깁니다. 왜 이럴까요?



챗룸 컴포넌트가 수많은 화면을 가진 큰 앱의 일부라 가정해봅시다. 유저가 chatroom Page에 도달하면, 컴포넌트는 마운트되고 connection.connect()를 호출할 것입니다. 그리고 이제 유저가 다른 화면으로 이동하는 것을 생각해봅시다. 챗룸 컴포넌트는 unMount 될 것입니다. 그리고 유저는 뒤로가기로 챗룸에 돌아오면 다시 챗룸이 마운트 될 것입니다. 이것은 두 번째 연결이니다. 하지만, 첫번째 연결을 사라지지 않았습니다. 계속 연결이 쌓여갑니다.



이 같은 버그는 광범위한 수동 테스트를 제외하고는 놓치기 쉽습니다. 이를 쉽게 발견할 수 있도록, 리액트는 개발단계에서 모든 컴포넌트를 첫 마운트 후 즉시 재마운트합니다.



연결 중이 두 번 나온 이유가 당신이 이런 실질적인 문제를 알아차리도록 돕습니다. 즉, 컴포넌트가 언마운트 될 때, 코드가 닫히지 않았습니다.



이 문제를 해결하려면 effect에서 cleanup function을 반환하십쇼

```
  useEffect(() => {
    const connection = createConnection();
    connection.connect();
    return () => {
      connection.disconnect();
    };
  }, []);
```

리액트는 매 번 Effect가실행되기전과 UnMount 시에 클린업함수를 실행할 것입니다. 



```
import { useState, useEffect } from 'react';
import { createConnection } from './chat.js';

export default function ChatRoom() {
  useEffect(() => {
    const connection = createConnection();
    connection.connect();
    return () => connection.disconnect();
  }, []);
  return <h1>Welcome to the chat!</h1>;
```

이 경우 연결-해제-연결 의 반응을 얻습니다.



이것이 개발의 올바른 행동입니다. 리액트는 구성 요소를 다시 마운트함으로써 이동 전 후 코드가 손상되는 지를 확인합니다. 해제와 그 후 연결은 정확하게 이루어져야합니다.  당신이 클린업을 잘 구현했다면, Effect를 한 번 실행한 것과 다시 실행한 것 사이에 사용자가 볼 수 있는 차이가 없어야합니다.



운영 환경에서, 당신은 연결중을 한 번만 보게될 것입니다. 다시 한번 마운트되는 것은 오직 개발중에만 발생합니다. strict mode를 해제하여 개발 동작을 해제할 수 있지만, 그대로 놔두기를 권장합니다.





# How to handle the Effect firing twice in development?

리액트는 의도적으로 컴포넌트를 두 번 마운트합니다. 올바른 질문은 어떻게 Effect를 한 번 실행하나요가 아나라, 어떻게 재마운트 후 작동하도록 이펙트를 수정하나요? 입니다.



주로 그 답은 클린업 펑션에 있습니다. 이펙트가 무슨 일을 하든 클린업 펑션은 정지하거나 실행취소해야합니다.  경험상, 유저는 이펙트 일회 실행과 반복실행과정의 차이를 구분할 수 없습니다. 



대부분의 이펙트 패턴은 아래 중 하나에 적합합니다.

### Controlling non-React widgets 

가끔씩은, 리액트로 쓰여지지 않은 UI 위젯을 추가할 때가 있을 것입니다. 

예를 들어, 페이지에 지도 컴포넌트를 추가하였다 생각해보겠습니다. 

이것은 setZoomLevel() 메서드를 가질 것이고, 당신은 React code의 zoom Level 상태변수와 동기화하여 확대/축소 수준을 유지하려합니다.

이 코드는 아래와 같습니다.

```
useEffect(() => {
  const map = mapRef.current;
  map.setZoomLevel(zoomLevel);
}, [zoomLevel]);
```

이 경우, 클린업은 필요없습니다. 개발환경에서 리액트는 두 번 호출할 것입니다. 그러나 여기에는 문제가 없습니다. 왜냐하면 setZoomLevel을 두 번 부르는 것은 아무 것도 아니기 때문입니다. 아마 조금 느려지겠지만 운영 환경에서는 다뤄지기 않기에 문제가 되지 않을 것입니다.



일부 API는 연속적으로 두 번 호출할 수 없습니다. 예를 들어, 기본 제공 <dialog> 요소의 showModal 메서드는 두 번 호출하면 느려집니다. 정리 기능을 구현하여 dialog를 닫도록 합시다.

```
useEffect(() => {
  const dialog = dialogRef.current;
  dialog.showModal();
  return () => dialog.close();
}, []);
```

  이는 다이얼로그를 한번만 시작한 것과 같은 효과를 지닙니다.



### Subscribing to events

 만약, 당신이 무언가를 구독한다면 클린업 펑션은 구독취소입니다.

```
useEffect(() => {
  function handleScroll(e) {
    console.log(window.scrollX, window.scrollY);
  }
  window.addEventListener('scroll', handleScroll);
  return () => window.removeEventListener('scroll', handleScroll);
}, []);
```

개발환경에서, 이펙트는 바로 addEventListner -> removeEventListner -> addEventListner를 다시 추가합니다. 따라서, 오직 하나의 활성화된 구독만이 남아있습니다. 이 운영환경에서 오직 한번만 호출하는 것과 동일한 환경이 됩니다.



# Triggering animations

만약, 애니메이션 효과가 이펙트 안에 있다면, 클릭업 펑션으로 초기값으로 초기화를 해줘야한다.

```
useEffect(() => {
  const node = ref.current;
  node.style.opacity = 1; // Trigger the animation
  return () => {
    node.style.opacity = 0; // Reset to the initial value
  };
}, []);
```



### Fetching data 

만약, 이펙트가 무언가를 가져온다면(fetch), 클린업 펑션은 패치를 중단하거나 결과를 무시해야합니다.

```
useEffect(() => {
  let ignore = false;

  async function startFetching() {
    const json = await fetchTodos(userId);
    if (!ignore) {
      setTodos(json);
    }
  }

  startFetching();

  return () => {
    ignore = true;
  };
}, [userId]);
```

이미 발생한 네트워크 요청을 취소할 수는 없지만, 클린업 함수를 이용하여 더 이상 무의미한 가져오기가 당신의 앱에 영향을 미치지 않도록 보장해야합니다. 

개발환경에서는 두 개의 네트워크 탭이 표시됩니다. 그것은 아무런 문제가 되지 않습니다. 위 방법대로 접근 시, 첫번째 이펙트는 즉시 무시되어서 더 이상 영향을 미치지 않습니다.



운영환경에서는 오직 하나의 요청이 있을 것입니다. 만약, 이런 중복요청이 당신을 괴롭힌다면, 컴포넌트간 중복요청을 제거하고 반응을 캐쉬하는 방법이 있습니다.

```
function TodoList() {
  const todos = useSomeDataLibrary(`/api/user/${userId}/todos`);
  // ...
```

이 방벙은 개발 경험을 향상시킬 뿐만아니라 당신의 애플리케이션을 더 빠르게 느끼게 할 것이다. 예를 들어, 뒤로 버튼을 누르는 사용자는 일부 데이터가 캐쉬되기 때문에 다시 로드 될 때까지 기다릴 필요가 없습니다. 이런 캐쉬는 직접 빌드하거나 수동 가져오기에 대한 여러가지 대안 중 하나로 사용할 수 있습니다.



### What are good alternatives to data fetching in Effects? 

fetch 를 Effects 내부에서 부르는 것은 클라이언트 사이드 앱에서 매우 인기 있는 방법입니다. 하지만, 이 방법은 수동적인 접근이며, 단점이 있습니다.

- 이펙트가 서버에서 실행되지 않습니다 .이 의미는 최초에 서버 렌더링 HTML은 데이터 없이 로드 상태만 포함한다는 것을 의미합니다. 클라이언트 컴퓨터는 모든 자바스크립트 파일을 다운받고, 렌더링을 한 이후에야, 이제 데이터 로드가 필요하다는 것을 알게 될 것입니다. 이것은 효율적이지 못합니다.
- 이펙트에서 직접 패치하는 것은 네트워크 waterfall를 쉽게 만들 수 있습니다. 부모님 컴포넌트가 렌더될 때, 데이터를 받아오고 자식을 렌더하고, 그리고 그들은 그들의 데이터를 받아옵니다. 만약, 네트워크가 느리다면 이것은 병렬적으로 데이터 가져오는 것보다 상당히 느릴 것입니다.
- 이펙트 내 다이렉트 패치는 캐쉬나 preload가 없다는 것을 의미한다. 예를 들어, 컴포넌트가 언마운트 된 후 다시 마운트 되면, 데이터를 또 패치해 올 것이다.
- 좋은 설계가 아니다(?) fetch 호출 시, race condition 같은 버그로 인해 어려움을 겪지 않도록 작성된 boiler plate가 상당히 많다.



이 단점은 마운트에서 데이터를 가져오는 모든 라이브러리(리액트 포함)에 적용됩니다. 이를 극복하기 위해서 아래와 같은 방법을 권장합니다.

- 모던 리액트 프레임워크는 위 같은 문제를 일으키지 않고 통합 데이터를 가져옵니다.
- 그렇지 않은 경우, 클라이언트 측 캐시를 사용하거나 만드는 것이 좋습니다. 유명한 오픈소스는 react-query, useSWR, React-router 6.4+가 있습니다. 그 외에도 Effect를 이용한 자체 솔루션을 구축하여, 후드 아래에서 중복 제거, 응답 캐싱, 네트워크 장애방지 로직을 설정할 수 있습니다.

이 두 방법 모두 맞지 않으면 계속 effects에서 fetch를 진행할 수 있습니다.



