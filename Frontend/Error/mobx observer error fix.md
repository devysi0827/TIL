 # mobx observer 사용과 에러

### observer 코드

```react
export default observer(function SideBarModal() {
  return (
    <ModalDiv>
      <ModalHeaderComponent />
      <ColorHr color="#EAEAEA" widthPercent="100%" />
      {SideBarStore.personaList.map((persona, personaIndex) => (
        <ModalContentComponent
          key={personaIndex}
          persona={persona}
          personaIndex={personaIndex}
        />
      ))}
      <ColorHr color="#EAEAEA" widthPercent="100%" />
      <ModalFooterComponent />
    </ModalDiv>
  );
});
```

- 이 경우 props(ModalContentComponent)가 제대로 재렌더링 되지 않음
- 또한, export default만 observer를 사용할 수 있어서 타 function에는 사용이 불가능했음



### 해결법

1. component 파일별로 분리시 문제 없이 observer를 걸어서 재랜더링 할 수 있음.
2. <Observer> 컴포넌트 사용 시, 해당 문제 해결

