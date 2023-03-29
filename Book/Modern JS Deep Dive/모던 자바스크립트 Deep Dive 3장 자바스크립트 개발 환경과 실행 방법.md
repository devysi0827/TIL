# **모던 자바스크립트 Deep Dive 3장 : 자바스크립트 개발 환경과 실행 방법**

### 자바스크립트 실행환경

Broswer와 Node.js 크게 두 가지 환경이 있으나, 둘이 제공하는 기능이 다르다.

Browser - EMCAScript 실행, DOM API 제공, Client Side API 제공

Node.js - EMCAScript 실행, File System 제공, Node.js 고유 API 제공

 

※ Node.js에서는 cheerio 같은 HTML Parsing 라이브러리를 이용하여, Node에서도 DOM 가공이 가능

※ Browser에서 File System이 제공될 시, 악성 JS파일이 브라우저를 통해 사용자의 컴퓨터를 쓰고 지울 수 있게된다. 즉, 해킹할 수 있다는 것이 된다. 그래서 제공하지 않고, FileReader API까지만 제공한다..

 



![img](https://blog.kakaocdn.net/dn/batDax/btr6NwMoylZ/ZqSOzWfkkDK9zGuDv3uWO0/img.png)



 

### Browser(Chrome 기준)

**개발자 도구** 

\- Elements :로딩된 웹페이지의 렌더링된 뷰를 확인 가능, 예상과 다를 시, DOM과 CSS를 편집해서 여기서 원인을 찾기 좋다.

\- Console : 로딩된 웹페이지의 에러를 확인하거나 자바스크립트 소스코드의 console.log 메서드의 결과를 알 수 있다.

\- Sources : 로딩된 웹페이지의 자바스크립트 코드를 디버깅할 수 있다.

\- Network : 로딩된 웹페이지에 관련된 네트워크 요청 정보와 성능을 확인할 수 있다.

\- Application : 웹 스토리지, 세션, 쿠키를 확인하고 관리할 수 있다.

 

**콘솔**

\- 에러가 표출되는 장소

\- 코드의 실행 결과를 확인하는 장소 (console.log)

\- REFL(Read Eval Print Loop) : 입력 수행 출력 반복이 가능한 환경

\- Shift + Enter를 누르면 줄 바꿈

 

**디버깅 (아래 링크 참조)**

 \- https://developer.chrome.com/docs/devtools/javascript/

 \- https://developer.chrome.com/docs/devtools/console/

 

### Node.js

npm (node package manager) : Node.js 모듈을 패키지 저장소 역할과 패키지 설치를 위한 CLI(Command line interface)를 제공한다.

 

**노드 접속하기**

명령 프롬프트에 **node** 를 입력하면, REPL을 이용하여, 자바스크립트 코드를 실행해 볼 수 있다.

이미 있는 파일을 실행할 때는 아래처럼 하면 파일을 실행할 수 있다.

```
node index.js
```

**ctrl +c** 를 두 번 누르면 node가 명령 프롬프트에서 종료된다.

 

### VSCode 

vscode는 매우 좋은 코드 에디터이며, 이를 이용하여 js를 실행할 수 있다.

\- 내장 터미널에서 "node 파일명" 을 통해서 실행할 수 있다.

\- **Code Runner** 플러그인을 사용하면 js 파일에서 ctrl + alt + n을 하면 js 파일이 실행된다.

\- **Live Server** 플러그인을 사용하면 js파일이 수정되었을 때, 자동으로 html에 수정사항을 반영해준다. (이 플러그인을 사용하지 않으면 다시 켜야한다.) 