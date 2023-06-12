# [WEB] SOP && CORS

웹에서 흔히 CORS 에러를 마주치고는 한다.

이 에러가 왜 발생하는 지 이유를 알아보고, 해결책을 찾아보자



### **출처란?**

먼저, 출처(Origin)을 알고 넘어가자.

![img](https://blog.kakaocdn.net/dn/xpnpZ/btsjFRK43nF/zuiAVO66Px2n2SJmxXgqHk/img.png)



위 사진에서, Protocol, Host, Port를 합친 것으로, 이 세 가지가 동일하다면 같은 출처라 정의한다.





### **SOP(Same-origin policy)란?**

SOP는 지난 2011년, [RFC 6454](https://tools.ietf.org/html/rfc6454#page-5)에서 처음 등장한 보안 정책으로 같은 출처(Origin)에서만 리소스를 공유할 수 있다는 정책이다.

이런 규제가 생긴 이유는 웹 보안을 강화하기 위해서입니다. 출처가 다른 두 애플리케이션이 쉽게 통신할 수 있다면, CSRF(Cross-Site Request Forgery)나 XSS(Cross-Site Scripting) 등의 공격에 너무나 취약해지기 때문에 보안을 강화하고자 이런 규제가 생기게 되었습니다.

다만, 다른 출처를 가진 웹에서 리소스를 가져오는 일은 매우 흔한 일입니다. 그래서 예외사항으로, CORS 정책을 지킨 리소스 요청은 출처가 달라도 허용하기로 하였습니다.



즉, CORS 에러는 CORS 정책을 지키지 않아서 SOP 정책에 의해서 브라우저가 리소스를 차단하면서 생기는 에러입니다. (이 때, 서버는 또 정상적으로 잘 응답했다 기록된다.)





### **CORS(Cross-Origin Resource Sharing) 과정**



위에서 설명한대로, 다른 출저 자원 공유 정책이며, 이 과정이 어떻게 진행되는 살펴보겠습니다.



1. 브라우저는 Origin을 HTTP 프로토콜을 이용하여 보내게됩니다.

2. 서버는 응답 헤더 Access-Control-Allow-Origin을 담아서 보내줍니다.

3. 브라우저는 응답을 받고, 요청 origin과 서버가 보내준 Access-Control-Allow-Origin을 비교하여 응답의 유효성을 판단합니다.

이 과정에서 유효하지 않으면, CORS에러가 발생합니다.

![img](https://blog.kakaocdn.net/dn/lK09v/btsjEmYV6Zj/e83LPn7bk98wbX1qf5zWh1/img.png)



### **해결방법은?**

대체로 세 개의 해결방법이 존재합니다.



**Access-Control-Allow-Origin 세팅하기** 

위에서 말했듯이, 서버가 Access-Control-Allow-Origin을 설정해주어서 안전한 출처임이 증명되면 됩니다. *(와일드카드)를 설정하면, 편하게 모든 출처가 리소스를 사용가능하나 반대로 서버의 보안이 위험해지기에 값을 제대로 설정하는 것이 좋습니다.



**reverse proxy** 

CORS 에러는 브라우저와 원하는 서버가 다른 출처이며 허용되지 않았기 때문에 발생합니다. 따라서, 바로 해당 서버와 브라우저가 통신하는 것이 아니라 중간에 모든 출처를 허용한 서버 대리점을 통해서 요청을 하는 방법이 있습니다. 자원 서버- 허용된 서버 간 통신 허용된 서버- 브라우저간 통신을 하는 것입니다. 즉, 프록시 서버를 이용하는 것입니다. 이 경우, API 요청 횟수 제한에 따라서 별도의 프록시 서버를 구축해야합니다.

![img](https://blog.kakaocdn.net/dn/6tZ8P/btsjGIs9TZ3/NJbcDkSVtWjElyNJR9pKx1/img.png)



**라이브러리 사용**

로컬에서 한정하여, http-proxy-middleware 라이브러리나 react나 vue의 설정을 조작하여 에러를 해결할 수 있습니다.



**참고자료**

mdn 공식문서 : https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

블로그 : [https://inpa.tistory.com/entry/WEB-%F0%9F%93%9A-CORS-%F0%9F%92%AF-%EC%A0%95%EB%A6%AC-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95-%F0%9F%91%8F](https://inpa.tistory.com/entry/WEB-📚-CORS-💯-정리-해결-방법-👏)

github : https://evan-moon.github.io/2020/05/21/about-cors/