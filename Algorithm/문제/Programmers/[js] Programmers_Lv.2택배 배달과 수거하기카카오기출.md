# **[js] Programmers_Lv.2_택배 배달과 수거하기_카카오기출**

### 문제

https://school.programmers.co.kr/learn/courses/30/lessons/150369

\- 최대 적재량이 정해진 차량이 있다. 배송할 택배와 수거할 택배량이 담긴 리스트가 존재하는데, 차량이 최소한으로 움직인 거리를 구하시오

 

### 아이디어

1. 가장 먼 곳부터 배달이나 회수하는 곳을 찾아가서 최대치 물량을 해결하고 오면 그게 가장 적게 움직이는 경우의 수가 된다.

 

### 구현(풀이)

```js
function solution(cap, n, deliveries, pickups) {
    let answer = 0;
    let point = n-1
    for (let i = point; i >= 0; i-- ) {

        while (deliveries[i] || pickups[i]) {
            answer += (i+1) * 2
            let rest = cap
            for (let j = i; j >= 0; j--) {
                if (deliveries[j]) {
                    if (deliveries[j] >= rest) {
                        deliveries[j] -= rest
                        break
                    } else {
                        rest -= deliveries[j]
                        deliveries[j] = 0
                    }
                }
            }

            rest = cap
            for (let j = i; j >= 0; j--) {
                if (pickups[j]) {
                    if (pickups[j] >= rest) {
                        pickups[j] -= rest
                        break
                    } else {
                        rest -= pickups[j]
                        pickups[j] = 0
                    }
                }
            }

        }
    }
    return answer;
}
```

1. 역으로 순회하면서, 배달 or 회수가 있는 공간에 도착한다. 

2. 1의 왕복거리 (i+1) * 2 를 정답에 더한다.

3. 해당 칸의 물건을 모두 배달/회수 한 후, 만약 남는 칸이 있다면, 다음 배달지를 찾아서 미리 배달 및 회수를 진행한다.

   

### 남의 풀이

```js
function solution(cap, n, deliveries, pickups) {
    let answer = 0;
    let give = 0;
    let get = 0;
    let cnt = 0;
    for(let i=n-1 ;i>=0;--i)
    {
        if(deliveries[i]!=0 || pickups[i]!=0)
        {
            cnt=0;
            while(give < deliveries[i] || get< pickups[i])
            {
                ++cnt;
                give+=cap;
                get+=cap;
            }
            give -= deliveries[i];
            get -=  pickups[i];
            answer = answer + ((i+1)*cnt*2);
        }
    }
    return answer;
}
```

\- 내가 만든 위 코드를 매우 깔끔하게 개량하여 사용하셨다. 난 저 코드를 더 개량하지 못했었다.

1. 마찬가지로 역순으로 순회하며 배달/ 회수가 있는 곳에 도착한다.

2. get과 give 수량을 조절한다. 이 때, 이 횟수를 cnt로 측정한다.

3. (i+1)*cnt*2로 총 거리를 answer에 합산하여 계산한다. 이 때, cnt = 0인 지점은 2번에 남은 양으로 해결하여 추가 방문할 필요가 없는 곳이다.



### 후기



![img](https://blog.kakaocdn.net/dn/bDIOFp/btsgtt6FhHh/9cvEsqRJvEyfk08wPDxOq0/img.png)

![img](https://blog.kakaocdn.net/dn/Vglk6/btsgpYlP6zY/CMWtkRNSOfKBIl0Z1nGMB0/img.png)



\- 핵심 로직은 똑같은데 구현력 차이와 불필요한 반복문이 줄어드니 코드 속력이 300배 정도 난다.

\- 스스로 풀 수 있지만 처음 풀었을 때는, 30점 나왔다. 나는 시간과 정확도에서 현재 굉장한 단점이 있다. 처음부터 꼼꼼하게 로직세워서 문제 푸는 버릇을 다시 들여야겠다.