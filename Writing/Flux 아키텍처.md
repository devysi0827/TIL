# Flux 아키텍처

### Flux 아키텍처란?

플럭스는 어플리케이션을 위한 데이터 흐름 관리 패턴입니다. 이 개념의 가장 중요한 점은 한 방향으로만 데이터가 흐른다는 것입니다. 

flux는 action, view ,store ,dispatcher 로 이루어집니다.



### Flux의 구성요소

**Dispatcher**

- 정의 : 디스패처는 actions를 수신하여 관련 스토어에 신속히 전달(dispatch)합니다.

- 특징 

  - **모든 스토어는 모든 액션을 수신합니다.**

  - 각 애플리케이션에는 싱글톤 디스패처가 하나만 있어야합니다.

※ 싱글톤 패턴 : 객체의 인스턴스가 오직 1개만 생성되는 패턴을 의미한다.



**Store**

- 정의 :스토어는 애플리케이션의 데이터를 저장합니다. 스토어는 애플리케이션의 디스패처를 등록하고 이를 통해서 액션을 수신합니다. 

- 특징 : 

  - **스토어의 데이터는 오직 액션에 응답함으로써만 변경될 수 있습니다.**

  - 스토어는 어떤 공공의 setter가 없어야만 합니다. 오직 getter만 있어야합니다.

  - 스토어는 응답해야할 작업(actions)을 결정합니다. 

  - 저장소의 데이터가 변경될 때마다, "변경" 이벤트를 전송해야합니다. 

  - 각 애플리케이션에는 많은 스토어가 있어야합니다.



### 참고문서

flux : https://github.com/facebookarchive/flux

flux concept : https://github.com/facebookarchive/flux/tree/main/examples/flux-concepts