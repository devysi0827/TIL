# ESLint와 React 안정성

### Error Name

Enforce a specific function type for function components (`react/function-component-definition`)



### 발생

```tsx
function TabButtons() {
  function Test() {
    return <div>t11est</div>;
  }

  return (
    <div>
      <Test />
    </div>
  );
}

```

이 코드는 기존에 사용하던 방식인데, 갑자기 위와 같은 같은 이름에 에러가 발생하였다. 읽어보니 정의되지 않은 컴포넌트를 사용하지 말라는데 무슨 말인가 싶어서 더 깊게 읽어봤다.



### 원인

구성 요소 내부에 구성 요소를 생성하면, React가 부모를 재렌더링 시, 중첩된 구성 요소의 상태를 버립니다.

아래 그림에서 Increase 버튼을 누른다면 1번 사진이 2번으로 바뀌도록 설계한 코드입니다.
하지만, 위에 나처럼 내부에 정의한  코드, 즉 초록색 영역의 코드는 자식의 상태를 가져오지 못했다.  

<img src='ESLint와 React 안정성.assets/image-20230102174024149.png'/>
<img src='ESLint와 React 안정성.assets/image-20230102174050919.png'/>


### 해결법

```tsx
function Test() {
  return <p>test</p>;
}

export default function TabButtons() {
  return (
    <div>
      <Test />
    </div>
  );
}
```

하란 대로 룰에 맞게 구성 요소 외부에 컴포넌트를 정의하면 된다.



### 예외 처리

```
"react/no-unstable-nested-components": ["error", { "allowAsProps": false }]
```

위와 같은 예외 룰을 `.eslintrc.json`에 설정하는 방법이 있다... 최적화를 포기하고 위와 같은 예외를 감수하겠다면 할 수는 있다...



### 참고

airbnb 문서 : https://github.com/airbnb/javascript#functions

airbnb 해결 문서 : https://github.com/jsx-eslint/eslint-plugin-react/blob/master/docs/rules/function-component-definition.md

airbnb 코드 예시 문서 : https://codepen.io/ariperkkio/pen/vYLodLB

