# git remote branch 가져오기

### 발생

팀원의 branch 내용을 확인이 필요했다.

하지만, git 사이트에는 존재하지만 내 로컬저장소에는 해당 branch가 존재하지 않았다.



### 원인

최초 clone을 만든 후 원격의 저장소로 업데이트 하지 않았기 때문이다.

(사실 로컬 작업을 하면 더 큰 브랜치만 가져와도 될 때가 있어서...)



### 해결

1). 원격 저장소를 업데이트 하자

```
git remote update
```

 2). 제대로 원격 저장소가 있는 지 확인해보자

```
git branch -a 
```

<img src='git remote branch 가져오기.assets/image-20230112231451393.png'/>
하양 - 로컬브런치, 초록 - 현재브런치, 빨강 - 원격브런치

없다면, 팀원이 원격에 올리지 않았는 지 확인해보자 

3). 원격 브런치로 전환한다.

```
git checkout remotes/origin/develop
```



하면 원하는 브런치가 뜬다!