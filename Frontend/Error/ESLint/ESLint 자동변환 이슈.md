# ESLint 자동변환 이슈

### 발생

```tsx
//1
const Test = () => {
  return <p>test</p>;
};

//2
function Test() {
  return <p>test</p>;
}
```

현재 프로젝트에 Test 컴포넌트를 1번과 같이 선언했을 때,  2번 코드로 바뀌는 현상이 있었다.

본래 우리 팀은 최상위 컴포넌트는 2번으로 그 외 컴포넌트는 1번으로 짜는 팀 내 규정이 있었는데, 이 때문에 찾아보게되었다.



### 원인

원인은 기존 프로젝트와 달리 airbnb style을 적용해서 그렇다.

ESLint는 2번 style을 기준으로 잡고 그 외는 틀린 것으로 처리하여 자동으로 변환해준다.



### 해결법

```
"react/function-component-definition": [<enabled>, {
  "namedComponents": "function-declaration" | "function-expression" | "arrow-function" | Array<"function-declaration" | "function-expression" | "arrow-function">,
  "unnamedComponents": "function-expression" | "arrow-function" | Array<"function-expression" | "arrow-function">
}]
```

위와 같은 예외 룰을 `.eslintrc.json`에 설정하면 된다. 

아래 공식문서를 참고하면 어떤 룰을 예외로 할 수 있는 지 구체적인 예시가 나온다. 

다만, 우리 팀의 경우 이 룰을 따라가면서 airbnb 룰을 체험해보기로 하였으며, 불편하면 추후 예외를 적용하기로 하였다.



### 참고

airbnb 문서 : https://github.com/airbnb/javascript#functions

airbnb 해결 문서 : https://github.com/jsx-eslint/eslint-plugin-react/blob/master/docs/rules/function-component-definition.md

