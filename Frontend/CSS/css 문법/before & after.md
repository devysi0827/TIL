# **: before & after** 

In CSS, **::before** creates a [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements) that is the first child of the selected element. It is often used to add cosmetic content to an element with the [content](https://developer.mozilla.org/en-US/docs/Web/CSS/content) property. It is inline by default.

 

element에 첫 번째 자식 요소(element) 인 pseudo-element를 만듭니다. 인라인이 디폴트로, 요소에 외관 요소를 추가하고자 할 때, 주로 사용됩니다.

 

※ pseudo-element : Html 요소의 특정 부분만을 선택하기 위한 요소입니다. 

 



![img](https://blog.kakaocdn.net/dn/bCSHQV/btr2D6d54FL/kqjJBMwYQkEcwekKukjsI0/img.png)



 

이 사진처럼, a tag 앞에 클립모양이나 커마 등의 문장 부호를 추가할 때, 주로 사용합니다. 그리고 해당 content와 관련된 내용에 CSS를 설정할 수 있습니다.

 

::after은 완전 반대요소로 content가 접미에 붙습니다.

 

참고문서

mdn : https://developer.mozilla.org/en-US/docs/Web/CSS/::before