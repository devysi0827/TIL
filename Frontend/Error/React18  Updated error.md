# React18  Updated error

### 원인

- 3/29일 리액트 업데이트로 인하여 기존 리액트17에서 쓰던 React-dom을 더이상 지원하지 않음

- React-dom 대신 React-dom/client(createRoot)를 사용하도록 개발자도구 콘솔에 Warning Message가 나옴.

- npx create-react-app 으로 만든 프로그램에서도 발생



### 해결방안

- index.tsx를 React-dom/clinet를 적용할 수 있도록 수정

```tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement,
);

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

```



### 참고문서

리액트 공식문서 : https://reactjs.org/blog/2022/03/08/react-18-upgrade-guide.html#updates-to-client-rendering-apis
스택오버플로 : https://stackoverflow.com/questions/71684417/upgrading-to-react18-and-react-dom18-fails