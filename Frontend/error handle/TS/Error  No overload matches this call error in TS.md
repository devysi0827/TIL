# Error : No overload matches this call error in TS

### 공부한 이유

- `Error : No overload matches this call error`이란 에러가 발생하였는데, overload가 뭔지 몰라서 공부를 시작하였다.



### 다형성

- 프로그램 언어의 다형성은 그 프로그래밍 언어의 자료형 체계의 성질을 나타내는 것으로, 프로그램 언어의 각 요소들(상수, 변수, 식, 오브젝트, 함수, 메소드 등)이 다양한 자료형(type)에 속하는 것이 허가되는 성질을 가리킨다. 반댓말은 단형성으로, 프로그램 언어의 각 요소가 한가지 형태만 가지는 성질을 가리킨다.

⇒ 쉽게 말하면, 하나의 클래스나 함수가 매우 많은 형태와 동작을 가질 수 있는 것을 의미합니다.

- overload 와 override은 각각 이 다형성을 구현하는 대표적인 방법이다.



### overload

- 두 메서드가 같은 이름을 가지고 있으나 인자의 수나 자료형이 다른 경우를 이를 하나의 메서드처럼 호출되게 하는 방법입니다.
- 함수의 기능이 동일하지만 인자의 종류와 형태 등등이 다르기 때문에 원래 다른 함수로 존재해야한다. 하지만, overriding을 이용하면, 메서드의 이름을 절약하고 가독성과 오류의 가능성 감소 등의 이점을 볼 수 있다.
- 대표적으로 `println()`이 있다. 이 함수는 “string”이든 “int”든 모두 동일하게 출력해준다. 하지만 `println()` 안에 인자는 분명 다른 타입의 변수를 받는다. 이는 다른 두 함수를 `println()`으로 통일한 뒤 타입에 맞게 함수를 선택 후 불러와서 편의성을 높인 것입니다. ⇒ 이는 다형성을 가질 수 있게합니다.



### override

- 상위 클래스의 메서드와 이름와 용례가 같은 함수를 하위 클래스에 재정의하는 것을 말한다.
- 개발자의 실수 방지를 위해서 `@Override`를 관례로 적는다.
- override 할 수 없는 조건들
  - static 메서드는 클래스에 속하는 메서드이기때문에 상속되지 않고 오버라이드되지 않습니다.
  - private 접근자도 마찬가지로 상속이 되지 않아서 오버리드가 성립되지 않습니다.
  - 오버로드와 달리 return type, method name, 매개 변수 패턴이 동일해야합니다.
  - final 지정되면 오버라이드 할 수 없습니다.
- 하지만, override는 마찬가지로 위 조건을 피했을 때, 다형성을 가질 수 있게 해줍니다.



### 예시

```java
class Cal{
    public int sum(int v1, int v2){
        return v1+v2;
    }
    // Overloading : 변수를 3개를 받는 함수를 새롭게 생성
    public int sum(int v1, int v2, int v3){
        return v1+v2+v3;
    }
}

class Cal3 extends Cal{
    public int minus(int v1, int v2){
        return v1-v2;
    }
    // Overriding : 기존의 함수에 출력을 하는 기능을 추가하여 새롭게 함수를 변경
    public int sum(int v1, int v2){
        System.out.println("Cal3!!");
        return v1+v2;
    }
 
}
```



### FE 에러

- Ts에서 발생하는 `Error : No overload matches this call error`의 의미는 결국, 해당 매개변수를 받는 이름의 컴포넌트나 함수가 존재하지 않아서 발생하는 에러이고, Component에서 해당 변수를 받고 사용할 수 있도록 미리 수정을 해두면 발생하지 않는 에러로 해결되었다.
- JS의 경우 이를 타입을 적는 칸이 없어서 이를 자동으로 수정을 해주니 발생하지 않는 에러여서 참신했다.



### 참고

- https://programmingnote.tistory.com/29
- https://opentutorials.org/course/4408/28703



