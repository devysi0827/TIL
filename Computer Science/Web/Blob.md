# Blob(Binary Large Object)

### 정의

- `Blob` 객체는 파일류의 불변하는 미가공 데이터를 나타냅니다. 텍스트와 이진 데이터의 형태로 읽을 수 있으며, [`ReadableStream`](https://developer.mozilla.org/ko/docs/Web/API/ReadableStream)으로 변환한 후 그 메서드를 사용해 데이터를 처리할 수도 있습니다.
- 주로 이미지, 비디오, 사운드 와 같은 멀티미디어 객체나 그 묶음을 의미합니다



### 생성

```javascript
var mBlob = new Blob(array, options);

ex).
var htmlCode = ['<!Doctype html>', 'Hello, World'];
var htmlBlob - new Blob(htmlCode, {
    type: 'text/html',
    endings: transparent
})
```



### 읽기

```js
1). FileReader
const reader = new FileReader();
reader.addEventListener('loadend', () => {
   // reader.result contains the contents of blob as a typed array
});
reader.readAsArrayBuffer(blob);

2).var text = await (new Response(blob)).text();
```



### 속성

1. Blob.size
2. Blob.type
3. Blob.slice
4. Blob.URL



### 참고문서

블로그 : https://sambalim.tistory.com/94 [삼바의 성장 블로그]

MDN: https://developer.mozilla.org/ko/docs/Web/API/Blob