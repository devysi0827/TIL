# **반응형 웹(Responsive Web)과 적응형 웹(Adaptive Web)**

### **서두** 

디자이너 분과 이야기하다가 반응형 웹과 적응형 웹에 대한 이야기가 나왔다.

적응형 웹이란 단어를 처음 들어봐서, 이에 대해 정리하고자 합니다.

 

### **반응형 웹(Responsive Web) 의 정의**

흔히 반응형 디자인의 창시자로 에단 마코트(Ethan Marcotte)를 거론합니다. 이전에도 개념은 존재했지만, 2010년에 아단 마코트가 **반응형**이란 용어를 처음 정의하였습니다.

 

반응형웹은 한 줄로 정의하면, **웹의 해상도, 레이아웃 등이 디바이스에 따라 반응하여 유동적으로 변환되는 웹페이지**입니다.

 

특히, Google은 2015년 4월 21일에 모바일 친화적인 사이트를 더 높게 평가한 [대규모 업데이트를](https://www.searchenginejournal.com/google-algorithm-history/mobile-friendly-update/#close) 출시한 이후 [항상 반응형 웹 디자인(RWD)을 권장해왔습니다.](https://developers.google.com/search/mobile-sites/mobile-seo/responsive-design)



![img](https://blog.kakaocdn.net/dn/byLitf/btr5OPtoEl9/koWFgaIQi8UPtWvf7OtA01/img.png)

​	디바이스에 따른 반응형 웹의 예시



 

일반적으로 미디어쿼리와 유동형 그리드와 유연한 이미지(Flexible Images)를 통해서 접속한 기기의 사이즈마다 웹페이지 형식을 조절해서 일관된 사용자 경험을 제공합니다.

 

하지만, 이처럼 너무 많은 정보를 담고 있는 사이트를 반응형으로 줄였을 때도 일관된 사용자 경험을 제공할 수 있는지, 동적 컨텐츠를 불러오면서 웹사이트의 성능이 저하되는 문제도 있다. 상황마다 다르겠지만 이런 부분들은 어렵다고 할 수 있다.

 



![img](https://blog.kakaocdn.net/dn/bSr5Ge/btr7OnVitJ6/RtGJIiDp9o0InoMw2VK6u0/img.png)



### **적응형 웹(Adaptive Web) 의 정의**



![img](https://blog.kakaocdn.net/dn/EdbEh/btr7OxcKgQJ/qlLoWc2oIukjB4fvzTFks0/img.png)



‘적응형 웹’이라는 용어는 Aaron Gustofson이 2011년 출간한 그의 책‘Adaptive Web Design: Crafting Rich Experiences with Progressive Enhancement’를 통해 처음 알려졌다.

 

위에서 서술한, 반응형웹이 모든 기기에 하나의 웹페이지를 크기별로 조절하는 것이라면, 적응형 웹은 대표적인 기기에 맞게 각각의 웹페이지를 만들고 접속한 기기에 맞는 웹페이지를 불러오는 방식이다. (사소한 기기 크기 차이는 비율 조절을 한다)

 

이런 개발 방식은 기기마다 별도로 코드를 관리할 필요가 없기 때문에 초기비용이 절감되며 유지보수가 편하고 가독성과 시스템 저하 문제를 해결할 수 있다. 실제로 기기별로 알맞은 콘텐츠(정보) 양의 제공, 불필요한 코드의 감소로 속도 향상, 기기에 맞는 코드로 유지보수 필요성 저하로 인해서 높은 만족도와 최적화된 사용자 경험을 제공하기 쉽습니다.

 



![img](https://blog.kakaocdn.net/dn/bcJnOV/btr7PjkLTQF/mHGJKVXMe4TxZnnkBMUycK/img.png)

속도 차이에 관한 글, 적응형이 훨씬 빠르다

 

예시로, [naver.com](http://naver.xn--com-rg8l/) 과 [m.naver.com](http://m.naver.xn--com-of0o/)을 볼 수 있다.

 

하지만, 이 역시 단점이 존재합니다. n 가지 페이지가 동시에 개발해야하므로 그에 따른 비용이 추가로 발생할 수 있으며, 하나의 페이지가 변경되며 n번의 수정이 필요해집니다. 그리고 모든 기기에서 일관되지 않은 컨텐츠가 있거나, 여러 url이 있는 것은 SEO에 부정적인 영향을 미칩니다.

 

### **결론**

자세히 보면 알겠지만, 두 디자인패턴이 명확하게 제시된 것은 2010년 초반이다.

둘 다 최신 디자인 패턴이며 아직 연구중인 디자인들이다. 그래서 위에서 서술한 것처럼 장점과 단점이 존재하며 이 부분을 아직 극복하지는 못했다.

하지만, 어떤 사이트에서는 이런 장점만 남고, 단점이 극단적으로 약해지기도 하고, 어떤 사이트에서는 부각되기도 하여서 이는 만드는 사이트가 어떤 사이트인지, 어떤 가치를 더 중요시하냐에 따라서 결정하면 좋을 것이라 생각한다.

 

### **참고** 

https://www.nextree.co.kr/p8622/

https://dataonair.or.kr/db-tech-reference/d-lounge/technical-data/?mod=document&uid=235777 

https://www.uxpin.com/studio/blog/responsive-vs-adaptive-design-whats-best-choice-designers/