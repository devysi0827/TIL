# CSS-charset

### 소개

```css
@charset 'utf-8';
```

기능 : CSS at-규칙은 스타일 시트에 쓰이는 문자 인코딩을 지정합니다.

용도 :  web or css 파일 인코딩 방식 설정, 'utf-8'은 전세계 모든 글자와 호환이 가능하고 메모리 낭비를 막을 수 있어서 사용함,

주의사항 :

- 스타일 시트 최상단 가장 처음에 와야함
- 여러 `@charset` at-규칙이 정의된 경우, 첫 번째 것만 사용되고 HTML 요소의 `style` attribute 또는 HTML 페이지의 문자 집합과 관련 있는 [``](https://developer.mozilla.org/ko/docs/Web/HTML/Element/style) 요소 내에서 사용될 수 없습니다.



### 참고문서

- 개인블로그 : https://pythontoomuchinformation.tistory.com/333
- mozila : https://developer.mozilla.org/ko/docs/Web/CSS/@charset

