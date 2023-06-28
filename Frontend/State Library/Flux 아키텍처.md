# **Flux Architecture** 

### Flux 아키텍처란?

- 플럭스는 어플리케이션을 위한 데이터 흐름 관리 패턴입니다. 이 개념의 가장 중요한 점은 한 방향으로만 데이터가 흐른다는 것입니다.
- flux는 action, view ,store ,dispatcher 로 이루어집니다.
- 현재는 폐기된 프로젝트이지만, 많은 상태관리 라이브러리가 이 아이디어를 근간으로 합니다.

 

### **Flux의 구성요소**

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

 

**Actions**

- 정의 : 애플리케이션의 내부 API를 의미합니다. 액션은 애플리케이션과의 상호작용을 모두 잡아내며, 타입과 데이터를 지낸 간단한 객체입니다.
- 특징
  - 액션은 시멘틱(의미론적)해야하며, 발생하는 행동을 설명해야합니다.
  - 액션은 액션의 상세한 구현사항을 설명해서는 안됩니다. 'delete-user-id', 'clear-user-data', 'refresh-credentials'를 사용하기 보다는 'delete-user'를 사용해야합니다. 모든 스토어는 작업을 수신하고, 동일한 액션(delete-user)을 통해서 해당 데이터를 지우거나 자격 정보(crendentials)를 갱신해야합니다.

 

**Views**

- 정의 : 스토어 내부 데이터가 보여지는 view입니다.
- 특징
  - 뷰로 어떤 프레임워크를 사용해도 괜찮습니다.
  - 스토어의 데이터를 사용하는 뷰는 해당 스토어의 변경 이벤트를 구독해야합니다. 그러지 않을 시, 버그가 생길 수 있습니다.
  - 일반적으로 유저와 애플리케이션의 상호작용이 일어날때, 뷰에서 액션을 발송합니다.

 

### **Flux 아키텍쳐 데이터 흐름도**



![img](https://blog.kakaocdn.net/dn/5ZROp/btslJfccybV/wizyNs82G49Ow8sP2lSknK/img.png)

1. view는 action을 dispatcher로 보냅니다.
2. dispatcher는 모든 store로 action을 보냅니다.
3. store는 view로 데이터를 보냅니다.

 



![img](https://blog.kakaocdn.net/dn/ZSolv/btslMb7e6Bh/kwB89oczVVN5bdQk4bTzx1/img.png)



이를 리액트에서는 위처럼 구체화할 수 있다.

 

### **참고문서**

flux : https://github.com/facebookarchive/flux

flux concept : https://github.com/facebookarchive/flux/tree/main/examples/flux-concepts