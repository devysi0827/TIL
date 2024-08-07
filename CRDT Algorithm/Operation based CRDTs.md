# Operation based CRDTs 

### 모르는 용어

- replication protocol

- Convergent Replicated (Data Type)
- vector clock
- eventsourcing
- F# , Akka.Net : 프로그램 종류 같은데 잘 모르겠음
- actor programming model
-  Reliable Causal Broadcast (RCB),



신뢰성 :

- 로컬에서 보이는 모든 업데이트는 결국 다른 노드에서 항상 보이게 되어야합니다.
  - 두 노드 사이 TCP 파이프를 놓으면 해결될 것처럼 보이나, 끊김과 연결이 지속적으로 발생할 수 있습니다.
  - 상태가 업데이트 될 때, 시스템이 종료되고 다시 시작될 수 있습니다.
  - 로컬의 커밋은 다른 피어들에게 공유되어야합니다. 그렇지 않다면, 비동기 상태에 빠집니다.
  - CRDT는 `즉각적인 응답`으로 잘 알려져 있습니다. 로컬에서 업데이트를 확인하기 전에 다른 노드가 업데이트를 받았는 지 확인할 필요가 없어야합니다. CRDT는 독립적으로 작동하도록 설계되었으며 우리는 이 속성을 유지하고자합니다.
  - evnet sourcing 방식은 작업을 지속하는 방법으로 알려져 있습니다. 이는 CRDT의 나머지 요구사항과 잘 맞아떨어집니다. 우리는 업데이트를 이벤트로 저장하고 필요할 때 재생할 것입니다. 이제 해야할 일은 이러한 업데이트를 다른 노드에 어떻게 복제할 지 알아내는 것입니다.





수정