# getElementByClassName Error in useEffect feat 조건부 렌더링

### 코드

```tsx
export default function MyEssayPage() {
  useEffect(() => {
    getMyEssay(1);
    const tests = document.getElementById("test");
    tests?.setAttribute("style", "red");
    console.log(test);
  }, []);

  return
    (
        <>
          {store.myEssayList.map((essay: any, Essayidx: any) => (
            <EssayListWrapper
              key={Essayidx}
            >
              <div>{Essayidx + 1}</div>
              <div>{essay.prompt.contents}</div>
              <div>{essay.essayContents}</div>
              <div id="test">{essay.score}</div>
            </EssayListWrapper>
          ))}
        </>
      )
}
```



### 원인

위 코드는 `useEffect`에서 `getMyData()`로 Api를 통해 데이터(`myEssayList`)를 불러온 후, 그 값을 조건부 렌더링 및 map을 이용하여서 배치하는 코드이다.

이 때, `myEssayList`에 데이터가 들어가는 중이므로, {} 내부는 null값으로 return 내부는 렌더링 되지 않는다. 

즉,` document.getElementbyId("test")`는 DOM에 없기 때문에 가져올 수가 없다. 



### 해결책

이 문제는 DOM접근이 아닌 다른 방법으로 해결했다. 왜냐하면, React에서 직접 DOM에 접근하는 방법은 지양하는 것이 좋다고 동료에게 조언을 받았기 때문이다. 하지만, 만약 꼭 이 방법을 써야한다면, useEffect를 하나 더 만들고 종속성변수를 `myEssayList`로 선정하면 아무 문제가 없을 것으로 생각한다.



### 느낀점

일주일 이상 붙잡으면서 많은 걸 공부하게 되었다. 공부한 내용 및 실수한 이유는 아래와 같다.

- stackoverflow를 잘못 해석했다. 그래서 useEffect가 원인이라 착각해버렸다. 덕분에 useEffect를 상세하게 알게되고 이 녀석은 문제 없음을 알게되었다.
- console.log("test")를 하면 잘 찍힌다. 이 녀석이 null값이라고는 생각을 못해봤는데, 웹 디버깅을 배워서 해보니 `tests` 변수가 null이였다. 덕분에 웹 디버깅도 배웠다.
- 예전부터 최초 실행만 하는 법을 열심히 찾았는데 찾다보니 useRef를 이용한 실행법을 찾았다. 이것도 연습해봐야겠다.
- React 공부가 아직 많이 필요하다 느낀다. 일단 기본적인 hook과 공식문서 정독을 해봐야겠다..