

#### Date: 0321

#  Django Ans

--------------------------------------------------------------ans-------------------------------------------------------

1). view



2). 응답이 url로 들어와 응답의 경로를 결정한다.



- 그 경로를 따라서 VIEW는 model에서 view로 데이터를 전송받고(데이터베이스관련요청일 겨웅), template에서는 양식을 받아서 해당 정보를 html등의 형식으로 응답해준다.



3). 4

- 파이썬 문법과 유사할 뿐 전혀 다른 언어이며 python코드로 실행되지 않는다.

4). {{variable|lower}}



5). 2

- 그외 기타등등이 더있다.



6). 이름을 지어줌으로써 절대 경로를 사용하지 않아서 수정이 용이하고, 특정 경로에 경우 경로에 대한 의존성을 줄일 수 있어서 편리해진다



7). variable rourting



8). 1

- 모델과 데이터베이스는 완전히 다르다.
- 레코드는 흔히 말하는 표의 행을 의미한다.
- makemigrations을 사용시 변경 모델을 기반으로 데이터베이스를 수정할 설계도를 만든다.



9). 우리는 orm을 사용함으로써, sql언어를 몰라도 db에 접근이 가능하며, db를 객체지향적 접근을 통해서 조작하기 때문에 높은 생산성을 얻을 수 있기 때문에 orm을 사용한다!



10). showmigrations



11).3

- 0개도 가능하다



12). #3번으로 사용시, Post('idx', 'title', 'content')라서 다르게 원하는 대로 적용되지 않는다.



13). 만약 정보가 POST 로 와서 유효하지 않았을 때, 오류를 막기 위해서 if-else문을 안이 아닌 동일 레벨에 작성한다.

- 제 답이 부실해서 각자 hw5-1번 답을 참고하시면 좋을 거 같아요!



14. settings.MEDIA_URL



15. 4

- 단순 raw한 렌더링 처리를 해준다



16. django.views.decorators.http 



17. `render` 는 템플릿을 불러오고, `redirect` 는 URL로 이동합니다. URL 로 이동한다는 건 그 URL 에 맞는 views 가 다시 실행될테고 여기서 render 를 할지 다시 redirect 할지 결정할 것 입니다. 이 점에 유의해서 사용하신다면 상황에 맞게 사용하실 수 있을 겁니다.



18. form.is_valid()



19. models.DateTimeField(auto_now=True)

