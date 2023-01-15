# css  우선순위

| 순위 | 선언방식           | 설명                                             | 예시                                                         |
| ---- | ------------------ | ------------------------------------------------ | ------------------------------------------------------------ |
| 1    | !important         | 우선순위 최상위 명령어. 속성값 바로 뒤에 넣는다. | `p { color: red !important; }`                               |
| 2    | inline style       | html 문서에서 tag 내에 style을 정의한 것         | `<p style="color: red">`                                     |
| 3    | id Selector        | tag 내에 id를 정의한 후, `#id` 으로 선택         | `<p id="title">제목</p>` `#title { color: red; }`            |
| 4    | class Selector     | tag 내에 class를 정의한 후, `.class` 으로 선택   | `<p class="subtitle">부제목</p>` `.subtitle { color: red; }` |
| 5    | tag Selector       | tag 요소를 선택자로 사용                         | `p { color: red; }`                                          |
| 6    | universal Selector | asterisk(`*`)로 요소 전체를 선택                 | `* { color: red; } `                                         |

다음과 같은 css 우선순위가 적용된다.

하지만 조금 어려운 예시로 아래와 같은 예시가 있다

```js
// js code
<div class="local-nav-links">
          <a href="#" class="product-name">right marign</a>
          <a href="#">left1</a>
          <a href="#">left2</a>
          <a href="#">left3</a>
</div>
```

```css
// css1
.local-nav-links .product-name {
  font-size: 1.4rem;
}
.local-nav-links a {
  font-size: 0.8rem;
}
```

```css
// css2
.product-name {
  font-size: 1.4rem;
}
.local-nav-links a {
  font-size: 0.8rem;
}
```

- css1 의 경우 font-size가 적용되지만 2의 경우는 적용되지 않는다.
- 이유는 a태그에 대한 상속들이 더욱 우선 적용되기 때문이다! id, !important 등을 사용할 경우 class보다 우선순위가 높아서 잘 적용이 된다! 



출처 : https://parkgaebung.tistory.com/72