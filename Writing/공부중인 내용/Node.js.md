# Node.js

### 정의

- JS를 실행하는 크롬 V8 엔진
- 브라우저 외부에서도 JS를 실행하는 실행환경(런타임)
- 서버로도 사용 가능
- express 라이브러리를 이용하여 서버 구축



### 장점

- 만들기 쉬워서 프로토타입 구축이 매우 쉬움
- 리얼타임서비스(스트리밍)에 유리 (넷플릭스)
- Non-blocking I/O
  - 요청을 먼저 받고, 빠른 순으로 처리
  - 요청이 많은 SNS 서버에서 유리
- ~~Event-driven~~



### 단점

- 라이브러리가 한정적(이미지처리 등이 타 서버에 비해서 불리)