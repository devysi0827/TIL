# [WEB] HTTP vs HTTPS

### **HTTP란?**

**정의** : HTTP(Hypertext Transfer Protocol)는 클라이언트와 서버 간 통신을 위한 통신 규칙 세트 또는 프로토콜입니다.

**원리** : HTTP는 OSI(Open Systems Interconnection) 네트워크 통신 모델의 애플리케이션 계층 프로토콜입니다. HTTP는 여러 유형의 요청과 응답을 정의합니다.

**문제점** : HTTP는 암호화되지 않은 데이터를 전송합니다. 즉, 브라우저에서 전송된 정보를 제3자가 가로채고 읽을 수 있습니다.

![img](https://blog.kakaocdn.net/dn/WyZOa/btsjmu9Sc4I/qmMllTVoK8McbGVOaOmGL1/img.png)

### **HTTPS란?**

**정의** : HTTPS는 위에서 설명한 보안상 문제점을 극복하기 위한 HTTP입니다. HTTPS 웹 사이트는 독립된 인증 기관(CA)에서 SSL/TLS 인증서(공개 키 구성요소)를 획득하여 이를 바탕으로 공개키와 세션키를 이용하여 암호한한 데이터를 전달합니다.



**암호화 방식**

- 대칭키 암호화 : 클라이언트와 서버가 동일한 키를 사용하여 암호화/복호화를 진행, 연산 속도가 빠른 장점이 있으나 키가 노출되면 위험
- 비대칭키 암호화 : 1개의 쌍으로 된 공개 키와 개인 키를 이용하여 암호화/복호화를 진행. 키가 노출되어도 상대적으로 안전하나 연산 속도가 느림

**통신과정**

- 최초 연결 시, 비대칭키 암호화 방식으로 세션 키를 교환합니다. 이는 최초에 보안을 확보하기 위해서입니다.
- 이후 통신 시, 위에서 교환한 세션 키를 이용하여 대칭키 암호화 방식으로 통신합니다. 위에서 보안을 확보했기 때문에, 속도를 위해서 대칭키 암호화 방식을 사용합니다.



**키 교환 과정 (client - server)**

1. 최초 접속 시, 브라우저(클라이언트)는 인증서(퍼블릭 키)를 요청하여 사이트의 신뢰성을 검증하려고 시도합니다. (인증서를 통해서 퍼블릭 키를 알 수 있습니다.)
2. 서버는 클라이언트에게 인증서(퍼블릭 키)를 전송합니다.
3. 웹 사이트의 SSL 인증서는 서버 아이덴티티를 증명합니다. 브라우저에서 인증되면, 브라우저는 세션 키를 생성하고 이를 퍼블릭 키로 암호화하여 전송합니다.
4. 웹 서버는 프라이빗 키를 사용하여 메시지를 해독하고 세션 키를 얻습니다. 이후, 클라이언트와 서버는 이 세션 키를 이용하여 대칭키 암호화 방식으로 통신합니다.

![img](https://blog.kakaocdn.net/dn/bMCdRO/btsjkiP2NcZ/DoavdZGDCkaslV64pMPTo1/img.png)

###  

### **HTTP vs HTTPS**

![img](https://blog.kakaocdn.net/dn/S0Bp5/btsjmuB3EmD/T8wmCh35hNyU6G1fU0m1m1/img.png)

###  

### **추가. HTTP/2, HTTP/3, HTTPS의 차이점은 무엇인가요?**

- HTTP/1.1 : 최초의 HTTP 버전 텍스트 형식으로 데이터를 전송
- HTTP/2 : 텍스트가 아닌 바이너리 방식을 이용하여 효율성 증가 및 클라이언트 캐시에 응답을 사전 전송 가능
- HTTP/3 : 실시간 스트리밍 및 최신 데이터 전송 요구사항을 효율적으로 지원하는 것이 목표



### **참고자료**

브런치 글 : https://brunch.co.kr/@hyoi0303/10

블로그 글 : https://mangkyu.tistory.com/98

아마존 문서 : https://aws.amazon.com/ko/compare/the-difference-between-https-and-http/