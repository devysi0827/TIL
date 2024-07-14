# State: A Component's Memory

[state-a-components-memory](https://react.dev/learn/state-a-components-memory)



글의 목적 : State의 개념 공유



### State란?

상호작용의 결과로써 화면의 내용을 변경해야할 때, 컴포넌트 해당 내용을 `기억`해야합니다. React는 이런 종류의 컴포넌트가 기억해야하는 메모리를 state라 부릅니다.



일반적인 지역 변수(local state)와 다른 점은 두 가지가 있습니다.

1. **지역 변수는 렌더링 사이에 유지되지 않습니다.** 두 번째로 렌더링 될 때, 지역 변수에 변경사항을 고려하지 않고 처음부터 다시 렌더링합니다.
2. **지역 변수를 변경해도 렌더링을 일으키지 않습니다.** React는 새로운 데이터로 컴포넌트를 다시 렌더링해야한다는 것을 인식하지 못합니다.



따라서 컴포넌트 다음 두 가지를 필요로 합니다.

1. 렌더링 사이에 데이터를 유지합니다. (State)
2. React가 새로운 데이터로 렌더링할 수 있도록 유발합니다. (state setter function)



위 두 가지를 `useState`  hook에서 제공합니다.



※ hook

Hook은 React가 렌더링 중에만 사용할 수 있는 특별한 함수로 `use`로 시작합니다.

이를 통해서 다양한 React 기능을 "연결"할 수 있습니다.

또한, hook은 import와 마찬가지로 최상위 수준에서만 호출할 수 있습니다. 조건문 또는 기타 중첩함수에서는 사용할 수 없습니다.





### useState

```react
const [index, setIndex] = useState(0);
```



위 함수는 다음과 같이 작동합니다.



1. **컴포넌트가 처음 렌더링 됩니다.** `index`의 초깃값으로 `useState`를 사용해 `0`을 전달했으므로 `[0, setIndex]`를 반환합니다. React는 `0`을 최신 state 값으로 기억합니다.
2. **state를 업데이트합니다.** 사용자가 버튼을 클릭하면 `setIndex(index + 1)`를 호출합니다. `index`는 `0`이므로 `setIndex(1)`입니다. 이는 React에 `index`는 `1`임을 기억하게 하고 또 다른 렌더링을 유발합니다.
3. **컴포넌트가 두 번째로 렌더링 됩니다.** React는 여전히 `useState(0)`를 보지만, `index`를 `1`로 설정한 것을 기억하고 있기 때문에, 이번에는 `[1, setIndex]`를 반환합니다.
4. 이런 식으로 계속됩니다!



### Component는 격리되고, 비공개이다.

또한, State는 격리되며, 비공개로 유지됩니다.



같은 컴포넌트가 있어도, 각 컴포넌트 내부의 State는 완전히 독립적이며 개별로 작동합니다.

또한, 호출된 컴포넌트(자식)는 선언한 컴포넌트(부모)에 대해여 완전히 독립적입니다. 

부모는 자식 컴포넌트에 영향을 주지 않기에 state에 추가/제거가 자유롭습니다.



만약, 두 컴포넌트가 state를 동기화해야한다면 [sharing-state-between-components](https://ko.react.dev/learn/sharing-state-between-components) 문서를 참조하여 자식 컴포넌트에 값을 제거하고, 부모 컴포넌트에 공통 state를 추가하여 사용하면 됩니다.



### 요약

- 컴포넌트가 렌더링 간에 어떤 정보를 “기억”해야 할 때 state 변수를 사용합니다.
- state 변수는 `useState` 훅을 호출하여 선언합니다.
- 훅은 use로 시작하는 특별한 함수들입니다. 이들은 state와 같은 React 기능에 “연결”할 수 있도록 해줍니다.
- 훅은 import와 마찬가지로 반드시 호출되어야 합니다. `useState`를 포함한 훅을 호출하는 것은 컴포넌트나 다른 훅의 최상위 수준에서만 유효합니다.
- `useState` 훅은 현재 state와 이를 업데이트할 함수로 이루어진 한 쌍을 반환합니다.
- 여러 개의 state 변수를 가질 수 있습니다. React 내부에서는 그들을 순서대로 매칭합니다.
- state는 컴포넌트에 비공개입니다. 두 곳에서 렌더링하더라도 각각의 복사본은 고유한 state를 가집니다.