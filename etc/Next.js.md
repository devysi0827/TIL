# Next.js

### 정의

**Next.js**는 [서버 사이트 렌더링](https://ko.wikipedia.org/wiki/서버_사이드_스크립트_언어), [정적 웹 페이지](https://ko.wikipedia.org/wiki/정적_웹_페이지) 생성 등 [리액트](https://ko.wikipedia.org/wiki/리액트_(자바스크립트_라이브러리)) 기반 웹 애플리케이션 기능들을 가능케 하는 [Node.js](https://ko.wikipedia.org/wiki/Node.js) 위에서 빌드된 [오픈 소스](https://ko.wikipedia.org/wiki/오픈_소스) 웹 개발 프레임워크이다.



+). React, Express.js, React-Router-Dom, SSR 의 기능을 내재화한 형태

+). code splitting



### 장점

1. 클라이언트 렌더링의 경우 모든 js 파일을 로드하고 사용자는 웹을 보게됩니다. 이때까지 사용자는 많은 시간을 대기해야 합니다.
2. seo 문제 - 클라이언트 사이드의 경우 자바스크립트가 로드 되지 않은 경우 아무런 정보를 보이지 않습니다. 구글의 검색엔진의 경우 자바스크립트가 로드되지 않은 페이지를 검색엔진으로 스캔함으로 결론적으로 검색에 아무 페이지도 걸리지 않게 됩니다.



### 기능

### hot reloading

개발 중 저장되는 코드는 자동으로 새로고침됩니다.

### automatic routing

pages 폴더에 있는 파일은 해당 파일 이름으로 라우팅됩니다. (pages/page1.tsx -> localhost:3000/page1)

public 폴더도 pages의 폴더와 동일하게 라우팅 할수있습니다. 그러나 모든 사람이 페이지에 접근할 수 있으므로 지양하도록합니다.

### single file components