# :not()

```
:not(selector) { style properties }
---
p:not(.classy) { color: red; }
body :not(p) { color: green; }
```

설명 : 부정(**negation**) [CSS 가상 클래스](https://developer.mozilla.org/ko/docs/Web/CSS/Pseudo-classes) `:not(X)`는 인수로 간단한 선택자(selector) X를 취하는 기능 표기법입니다. 인수로 표시되지 않은 요소와 일치합니다. X는 다른 부정 선택자를 포함해서는 안 됩니다.



용도 : 특정 클래스 예외처리 



출처: https://developer.mozilla.org/ko/docs/Web/CSS/:not