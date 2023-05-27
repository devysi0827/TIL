# react 'fs module not found' 해결하기

### 해결법

- Package.json 마지막줄에 아래 코드를 붙여 넣는다.

  ````json
  "browser": {
      "fs": false,
      "path": false,
      "os": false
    },
  ````



### 참조

https://exerror.com/module-not-found-error-cant-resolve-fs-in/