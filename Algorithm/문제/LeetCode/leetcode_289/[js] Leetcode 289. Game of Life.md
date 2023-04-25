# [js] Leetcode 289. Game of Life

### 문제

https://leetcode.com/problems/game-of-life/description/

배열을 순회하면서 각 칸의 이웃의 개수가 다음 조건을 만족하면 바꿔라

\- 살아있는 칸(1):

이웃의 살아있는 칸이 0,1개 : 죽은 칸(0)으로

이웃의 살아있는 칸이 2,3개 : 살아있는 칸(1)으로

이웃의 살아있는 칸이 3개 초과 : 죽은 칸(0)으로



\- 죽은 칸(0):

이웃의 살아있는 칸이 정확히 3개 : 살아있는 칸(1)으로



return하는 값은 없고 원본이여야한다.( Do not return anything, modify board in-place instead.)



### 아이디어

1. 원본 배열을 복사한다. (원본이 수정되면 아래 함수의 기준이 바뀌어서 다른 값이 된다. 기준값은 불변해야한다.)

2. 8방향의 생존칸의 개수를 세는 함수를 만든다. 최종적으로 생존칸 && 2 or 3이면 1을 리턴 아니면 0을 리턴한다. 

3. 이 때, 4개 이상, 1개 이하이면 리턴한다. (가지치기) 

4. 순회하면서 해당 함수를 돌리며 원본을 수정한다.



### 구현(풀이)

```
/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */

var gameOfLife = function(board) {
    const m = board.length
    const n = board[0].length
    const copyBoard = JSON.parse(JSON.stringify(board));
    const direction = {
        upright : [-1,-1],
        up : [-1,0],
        upleft : [-1,1],
        right : [0,-1],
        left : [0,1],
        downright : [1,-1],
        down : [1,0],
        downleft : [1,1],
    }

    function game(x,y) {
        let cnt = 0
        const keys = Object.keys(direction)
        for (let i = 0; i< keys.length; i++){
            const value = direction[keys[i]]
            const dx = x + value[0]
            const dy = y + value[1]
            if (dx >=0 && dx <m && dy >=0 && dy <n){
                if (copyBoard[dx][dy] === 1){
                    cnt +=1
                    if (copyBoard[x][y] === 0 && cnt >=4 ){
                        return 0
                    }
                }
            }
        }
        if (cnt ===2 && copyBoard[x][y] === 1){
            return 1
        }
        if (cnt === 3) {
            return 1
        }
        return 0
    }

    // const copyBoard = _.cloneDeep(board)
    // const copyBoard = Array.from(Array(m), () => Array(n).fill(0))
    
    for (let i = 0; i < m; i++){
        for (let j =0; j <n; j++){
            board[i][j] = game(i,j)
        }
    }

    // return copyBoard
};
```

1. 알고리즘에서는 deepcopy로 lodash함수를 사용할 수 없나보다.. 그냥 **JSON.parse(JSON.stringify(board))** 를 사용하자

2. 시간복잡도는 O(mn) => O(n^2)인 거 같다. .



※ 처음에는 빈 2차 배열 만들려했는데, python이 아니니 또 벙져버렸다. 풀이랑은 직접적인 연관성은 없으나 아래처럼 만들 수 있다.

```
const copyBoard = Array.from(Array(m), () => Array(n).fill(0))
```



### 남의 풀이

```
var gameOfLife = function(board) {
    if(board.length === 0){
        return board;
    }
    
    var checkNeighbors = function(row, col){
      var score = -board[row][col];
      var r, c;
      for(r = row - 1; r <= row + 1; r++){
          for(c = col - 1; c <= col + 1; c++){
              if(typeof board[r] !== "undefined" && typeof board[r][c] !== "undefined"){
                score += Math.abs(Math.floor(board[r][c]));
              }
          }
      }
      return score;
    };
    
    var r, c;
    for(r = 0; r < board.length; r++){
        for(c = 0; c < board[0].length; c++){
            var score = checkNeighbors(r, c);
            if(board[r][c] === 1){
                if(score < 2 || score > 3){
                    board[r][c] = -0.5;
                }
            }
            else if(board[r][c] === 0){
                if(score === 3){
                    board[r][c] = 0.5;
                }
            }
        }
    }
    
    for(r = 0; r < board.length; r++){
        for(c = 0; c < board[0].length; c++){
            board[r][c] = Math.ceil(board[r][c]);
        }
    }
};
```



### 참고문서

array.from : https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/from