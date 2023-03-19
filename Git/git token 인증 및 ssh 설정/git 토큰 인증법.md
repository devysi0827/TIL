# git 토큰 인증법

### Git push 시 생기는 password 문제

- 문제점: push를 할 때 username과 password를 물어보는데 git username과 password를 사용할시 에러가 발생한다
- 문제의 원인: 기존의 password 인증 대신 token 인증으로 인증법이 바뀌어서 password인증은 더이상 인증되지 않는다.
- 해결방법

1. git hub 로그인 > 프로필 아이콘 클릭 > Settings 클릭 > 왼쪽 사이드바 최하단 Devoloper settings > personal access tokens 클릭

![Git 토큰 인증법1](git 토큰 인증법.assets/Git 토큰 인증법1.png)

2. generate new token 클릭
   ![Git 토큰 인증법2](Git 토큰 인증법.assets/Git 토큰 인증법2.png)

   ![Git 토큰 인증법3](git 토큰 인증법.assets/Git 토큰 인증법3.png)

3. token 생성
   - 만료일 설명등도 각자 설정
   - 필요한 부분들을 선택하고 생성(잘 모르면 모두 선택하자)
   - 그 후 생성된 토큰을 복사하자!

![Git 토큰 인증법4](git 토큰 인증법.assets/Git 토큰 인증법4.png)

4. ![Git 토큰 인증법5](git 토큰 인증법.assets/Git 토큰 인증법5.png)터미널에서 비밀번호 대신 사용하기

![Git 토큰 인증법6](git 토큰 인증법.assets/Git 토큰 인증법6.png)

cf). 토큰은 절대 공유하면 안됩니다!!!!!!!! 큰일납니다!!!!!!!!!!!!!!! (위토큰도 바로 삭제했습니다)

cf2). 3에서 token을 생성할 때 적절하게 생성하지 않는다면 403에러가 발생합니다