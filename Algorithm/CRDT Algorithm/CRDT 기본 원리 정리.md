# CRDT 기본 원리 정리

https://www.youtube.com/watch?v=B5NULPSiOGw

- 데이터주도 어플리케이션 추천

### 1:23 - 인트로

- 동시 편집은 동시에 작업이 시작하여, 화면에서 동시에 종료되길 원한다. 이런 속성을 convergence property(수렴 속성)라 한다.
- 합의와 비슷해보이지만 매우 다른 이야기이다.

### 2:30 - 시작

- git은 자동으로 문서를 병한한다. 하지만, 같은 줄을 편집한 경우에는 수동으로 편집해야한다.

  ![image-20240803234758847](C:/Users/sell/AppData/Roaming/Typora/typora-user-images/image-20240803234758847.png)

- 구글 docs

  - 데이터에 수정이 일어날 때, 로컬 복사본에 먼저 사용자의 입력을 반영한 뒤, 서버로 수정사항을 전달한다.

  - 하지만 여기서는 동시성 문제가 발생합니다. (서버로부터 응답을 받아서 다시 수정해야하기 때문에)

    ![image-20240803234809686](C:/Users/sell/AppData/Roaming/Typora/typora-user-images/image-20240803234809686.png)

  - 오프라인 편집이 있을 때 이 부분이 더욱 부각됩니다. 로컬에서만 체인지를 가지고 있다가 네트워크가 연결되면 그 때 모든 변경사항을 flush합니다.

    - flush : 임시 저장소에서 영구 저장소로 이동하는 것

### 6:27 - 실제로 자료구조를 어떻게 통합할까?

- 구글이 통합하는 법

  ![image-20240803234827693](C:/Users/sell/AppData/Roaming/Typora/typora-user-images/image-20240803234827693.png)

  ![image-20240803234835505](C:/Users/sell/AppData/Roaming/Typora/typora-user-images/image-20240803234835505.png)

  - git이라면 이 부분이 병합 충돌되어서 수동으로 해결하라 할 것입니다. 하지만, 구글 doc는 그러지 않습니다.
  - 각 단어는 순서가 있으므로 합리적으로 이렇게 통합할 수 있습니다.

  ![image-20240803234843460](C:/Users/sell/AppData/Roaming/Typora/typora-user-images/image-20240803234843460.png)

  - 이 부분은 텍스트에 국한되지 않습니다.

  ![image-20240803234852411](C:/Users/sell/AppData/Roaming/Typora/typora-user-images/image-20240803234852411.png)

  ![image-20240803234859818](C:/Users/sell/AppData/Roaming/Typora/typora-user-images/image-20240803234859818.png)

- counter를 고려하면 값은 증분도 고려해야한다는 걸 알 수 있습니다. (데이터를 캡쳐해야한다)

# 9:58 - CRDT의 탄생

![image-20240803234910315](C:/Users/sell/AppData/Roaming/Typora/typora-user-images/image-20240803234910315.png)

- 동시편집에 대한 연구는 계속되었으나, OT는 몇 가지 문제로 인하여 CRDT가 대두되었음

  ![image-20240803234918176](C:/Users/sell/AppData/Roaming/Typora/typora-user-images/image-20240803234918176.png)

- 각 논문들은 수렴에 도달하지 못하였음 (수렴 : 최종적으로 같은 데이터가 화면에 표출되어야함)

- 그리고 중앙 서버가 존재해야한다는 결론에 도달함.

![image-20240803234926019](C:/Users/sell/AppData/Roaming/Typora/typora-user-images/image-20240803234926019.png)

- 각 유저는 반드시 중앙 서버를 거쳐야만 함 (그렇지 않을 경우, 절대로 수렴에 도달하지 못함)
- 이는 네트워크의 낭비를 의미함. (가까이 있더라도 반드시 버지니아의 데이터 센터를 거쳐야만함)
  - 토폴로지 :네트워크 연결 장치들이 어떻게 연결되어 있는 지를 의미. (데이터의 흐름)

![image-20240803234933055](C:/Users/sell/AppData/Roaming/Typora/typora-user-images/image-20240803234933055.png)

- 분산시스템이 탈중앙화 되는 것이 정말 매력적인 것이라 생각함
  - 현재는 구글 네트워크가 동작하지 않으면 동작하지가 않고  이는 굉장히 아쉽다는 생각이 듬.

# 14:26 - 블록체인

![image-20240803234940135](C:/Users/sell/AppData/Roaming/Typora/typora-user-images/image-20240803234940135.png)

![image-20240803234947559](C:/Users/sell/AppData/Roaming/Typora/typora-user-images/image-20240803234947559.png)

- 합의(pick one) - 특정 값을 선택하고 나머지 수정사항을 버리는 과정
- 수렴(keep all) - 모든 수정사항을 통합하여 하나의 결과값을 만드는 과정

# 18:10 - Proving CRDTs Correct

![image-20240803234955159](C:/Users/sell/AppData/Roaming/Typora/typora-user-images/image-20240803234955159.png)

- isabelle(수학 증명 시스템)을 이용하여 프로그램 작성하여 특정 가정하에 일관성을 보임을 증명함.
- 네트워크 모델을 통해서, 실제로 동작함을 증명함.

논문 :

[Verifying Strong Eventual Consistency in Distributed Systems](https://www.repository.cam.ac.uk/items/444a8851-252b-45ea-87a3-be9ca4e9530c)

# 20:02 - Automerge

- webRTC로 네트워크 없이 가능하다. (P2P로)
- automerge는 데이터 추상화 계층이며, 데이터 모델이다.
- websocket

# 26:29 - AutoMerge의 원리

- 불변성 개념을 이용하여, 명령형 프로그래밍을 진행함
  - change 함수에 변경사항과, commit Message를 전달하며 새로운 객체를 반환함
  - 이 메시지를 이용하여 맵 객체에 log를 남김
  - 이를 통해서 “시간 여행” 이 가능함.

# 30:10 - 동시성

동시 편집 상황이 발생했을 때,

1. 각 사용자는 각자의 로컬에 편집 사항을 반영합니다. (네트워크의 독립적임)
2. 네트워크가 있을 경우, 변경사항을 전파합니다.

# 32:14 - Conflict

충돌이 발생했을 때,

1. 기본값을 선택한다.
2. merge 충돌을 알리고, 사용자에게 선택권을 제공한다.
   1. nutshell : 간결한 설명 , 요약

![image-20240803235004150](C:/Users/sell/AppData/Roaming/Typora/typora-user-images/image-20240803235004150.png)

텍스트의 경우, 이런 식으로 모두 킵하는 방식으로 merge 될 수 도 있다

이 부분은 무작위지만 결정적이다. (node 문자는 각각의 ID를 가진다)

![image-20240803235011992](C:/Users/sell/AppData/Roaming/Typora/typora-user-images/image-20240803235011992.png)

- 다른 위치에 대해서, 식별자를 이용하여 추가하고 이를 받아서 넣으면 된다.

# Insertions - 같은 위치에 삽입이 일어났을 때

![image-20240803235019443](C:/Users/sell/AppData/Roaming/Typora/typora-user-images/image-20240803235019443.png)

- skip 규칙 : 작업하려는 아이디보다 큰 아이디를 만나면 skip한다. 작다면 멈추고 insert한다.
  - 최초 삽입 위치를 정한다. (이 경우, 1a다)
  - 1a 이후 4a보다 작은 것을 만날 때가지 전진한다. 4b,5b가 크므로 skip 한다.
  - 2a는 4a보다 작다. 멈추고 삽입을 진행한다.