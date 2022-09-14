# useEffect

- 정의 : React에게 컴포넌트가 렌더링 이후에 어떤 일을 수행해야 하는 지를 지시, React는 우리가 넘긴 함수를 기억했다가(이 함수를 `effect`라고 부릅니다) DOM 업데이트를 수행한 이후에 불러냄

- 발동 타이밍 : 첫 렌더링 이후, 매 업데이트마다

- 분류: 크게 clean-up이 필요한 경우, 필요하지 않은 경우로 나뉘어집니다.

  

### 기존 React lifeCycle과 비교

- useEffect는 `componentDidMount` ,`componentDidUpdate`, `componentWillUnmount` 가 합쳐진 역할을 수행함
- `componentDidMount` : 최초 실행 시 컴포넌트 렌더링 이후 effect를 실행
- `componentDidUpdate` : [] 안에 변수에 변화를 감지하여 update를 실행
- `componentWillUnmount` : 구독 등 정리(clean-up)가 필요로 할 경우, return 문으로 해당 기능을 사용가능함.



### 렌더링

- useEffect에서 effect(전달된 함수)는 매 번 다른 effect로 교체하여서 작동합니다.

​	⇒ 이는 상태 값이 제대로 업데이트 되도록 일부러 react에서 설정한 방식입니다.

​	⇒ 이 부분과 관련하여서 [] 안에 변수를 넣음으로써, 이전 `prevState`와 비교하여서 최적화를 진행합니다.

​	⇒ useEffect 내 [] 변수가 `prevState` 와 동일하다면, 건너뛰고 아니라면 업데이트한 state로 useEffect를 실행합니다.

​	⇒ 따라서, 최적화와 관련하여서 []안의 변수(종속성 변수)를 포함했다면 []안을 설정해주는 것이 좋습니다.

- `useCallback` 으로 감싸서 Effect를 의존성 배열 함수를 추가할 시, 자체 종속성이 변하는 경우에만 리렌더링이 실행됩니다.

```jsx
const fetchProduct = useCallback(() => {
    // ... productId로 무언가를 합니다 ...
  }, [productId]); // ✅ 모든 useCallback 종속성이 지정됩니다
```

- 종속성 변수가 만약 너무 자주 변경된다면, 종속성 변수에 의존하지 않고 콜백 변수를 사용하는 것이 좋음

```jsx
//... error code
function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      setCount(count + 1); // 이 effect는 'count' state에 따라 다릅니다
    }, 1000);
    return () => clearInterval(id);
  }, []); // 🔴 버그: `count`가 종속성으로 지정되지 않았습니다

  return <h1>{count}</h1>;
}

//... good code
function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const id = setInterval(() => {
      setCount(c => c + 1); // ✅ 이것은 외부의 'count' 변수에 의존하지 않습니다
    }, 1000);
    return () => clearInterval(id);
  }, []); // ✅ 우리의 effect는 컴포넌트 범위의 변수를 사용하지 않습니다

  return <h1>{count}</h1>;
}
```

### 참고문헌

- https://stackoverflow.com/questions/69849494/why-is-document-getelementsbyclassname-not-working-in-react
- https://ko.reactjs.org/docs/hooks-faq.html#is-it-safe-to-omit-functions-from-the-list-of-dependencies