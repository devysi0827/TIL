# Mobx 개론 및 요지

### Mobx란?

functional reactive programming를 적용하여 쉽게 비동기 데이터 변경과 렌더링 최적화를 자동으로 만들어주는 상태관리 라이브러리입니다. 



※ functional reactive programming : 



### 기본 예제

![image-20230104135403723](Mobx 개론.assets/image-20230104135403723.png)

1. 모든 event(click... )는 observable state를 변경시키는 action을 호출합니다.
2. 변화한 observable state는 모든 연산값과 관련된 부수효과(리액토 컴포넌트)에 전파됩니다. 



### Mobx의 요지

```js
class Todo {
    id = Math.random()
    title = ""
    finished = false

    constructor(title) {
        makeObservable(this, {
            title: observable,
            finished: observable,
            toggle: action
        })
        this.title = title
    }

    toggle() {
        this.finished = !this.finished
    }
}
```



1. 상태(State) : 애플리케이션을 구동하는 데이터입니다.

   - 관찰 가능한(observable) : 시간이 지남에 따라 변경하려는 모든 속성을 Mobx가 추적할 수 있도록 `observable`로 표시합니다.

   -  비유하면, 값을 보유하고 있는 스프레드시트 셀과 같습니다.

   

2. 동작(Action) : 이벤트에 따라서 state를 변경하는 코드 조각(Methods)입니다.

   - `observable`을 변경하는 코드 

   - 비유하면, 스프레드 시트 셀에 새 값을 입력하는 것입니다.

   - 현재의 state를 기반으로 새로운 정보를 계산하는 view와 대조적입니다.

   

3. 파생(Derivation) : state에서 더 이상의 상호작용 없이 파생될 수 있는 모든 것이 derivation입니다.

   - ex). 사용자 인터페이스, 파생 데이터, 백엔드 통합(서버 변경사항 등)

   - 파생의 종류

     - computed : 현재의 observable state에서 순수 함수를 사용하여 파생될 수 있는 값
     
     - reaction : state가 변경될 때, 자동으로 발생해야하는 부수효과입니다. 명령형 프로그래밍과 반응형 프로그래밍을 이어주는 다리 역할을 수행합니다. UI 컴포넌트에서 많이 사용됩니다. 
     
     - computed 와 reaction 차이 :  reaction은 computed 값과 유사하지만, 정보를 생성하는 대신 콘솔 출력, 네트워크 요청, DOM 패치 적용을 위해 React 컴포넌트 트리를 점진적으로 업데이트하는 등의 부수효과를 생성합니다. 즉, 반응형 프로그래밍과 명령형 프로그래밍의 세계를 연결합니다.
     
     - reaction을 과도하게 사용하지 않고 state를 기반으로 값을 생성하려는 경우 항상 computed를 사용하는 것이 좋은 방식입니다.
     
       

※  명령형 프로그래밍 : 무엇(What)을 할 것인지 나타내기보다 어떻게(How) 할 건지를 설명하는 방식. 

- 예시로 C, C#, Java
- 분류로 절차지향, 객체지향 프로그래밍이 존재

※  선언형 프로그래밍  : 어떻게 할건지(How)를 나타내기보다 무엇(What)을 할 건지를 설명하는 방식. 

- 예시로, SQL, 하스켈, 리스프 등이 존재
- 분류로 함수형 프로그래밍이 존재

​     

4. computed를 사용하여 파생된 값 모델링하기

   - *computed* 값을 생성하려면 JS getter 함수 `get`을 사용하여 속성을 정의하고 `makeObservable`을 사용하여 `computed`로 표시합니다.

     ```js
     class TodoList {
         todos = []
         get unfinishedTodoCount() {
             return this.todos.filter(todo => !todo.finished).length
         }
         constructor(todos) {
             makeObservable(this, {
                 todos: observable,
                 unfinishedTodoCount: computed
             })
             this.todos = todos
         }
     }
     ```

※  getter : 프로퍼티를 읽으려할 때, 실행하는 메서드 

※  setter : 프로퍼티의 값을 할당하려할 때, 실행하는 메서드



5. 리액션을 사용한 부수효과 모델링하기

   - 트리거가 될 수 있는 명확하고 명시적인 출저가 있는 부수효과는 관련 이벤트 핸들러에서 명시적으로 트리거가 되어야합니다. (표시해야한다는 말인듯)
   - 





※  순수함수 : 외부의 상태값을 참조하거나 변경하지 않는 함수로 동일 인자를 넣으면 동일 값을 반환해야한다.





### 참고

https://ko.mobx.js.org/README.html

https://ko.mobx.js.org/getting-started.html
