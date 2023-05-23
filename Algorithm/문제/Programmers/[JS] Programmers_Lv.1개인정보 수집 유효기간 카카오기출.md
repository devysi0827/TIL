# **[JS] Programmers_Lv.1_개인정보 수집 유효기간_ 카카오기출**

### **문제**

[ 프로그래머스코드 중심의 개발자 채용. 스택 기반의 포지션 매칭. 프로그래머스의 개발자 맞춤형 프로필을 등록하고, 나와 기술 궁합이 잘 맞는 기업들을 매칭 받으세요.programmers.co.kr](https://school.programmers.co.kr/learn/courses/30/lessons/150370)

약관에 따라 일정 기간 후 개인정보가 만료된다.

오늘날짜와 가입정보(날짜, 약관종류)의 배열을 보고 만료된 개인정보를 담은 배열을 반환하시오.

 

### **아이디어**

1. 객체의 약관에 대한 데이터들을 저장하자.

2. 가입정보 배열을 순회하면서, 가입정보에 약관기간을 더한 후 현재 날짜와 비교한다. 초과한 배열을 모아서 반환한다. 

 

### **구현(풀이)**

```
function solution(today, terms, privacies) {
    let [sYear,sMonth,sDay] = today.split('.').map(x=> parseInt(x))
    let termObj = {}
    for (let i =0; i< terms.length; i++){
        const [alpa, exp] = terms[i].split(' ')
        termObj[alpa] = parseInt(exp)
    }

    let result = []
    for (let i =0; i< privacies.length; i++){
        const [thisToday, thisTerm] = privacies[i].split(' ')
        let [year,month, day] = thisToday.split('.').map((x)=> parseInt(x))
        month += termObj[thisTerm]
        if (checkprivacy(year,month,day)){
            result.push(i)
        }
    }


    return result.map(x=>x+1)

    function checkprivacy(year,month,day) {
        let plusYear = 0
        let rest = month
        while (rest > 12){
            rest -= 12
            plusYear +=1
        }

        year += plusYear

        if ( year < sYear){
            return true
        }
        if (year === sYear && rest < sMonth) {
            return true
        }
        if (year === sYear && rest === sMonth && day <= sDay) {
            return true
        }
        return false

    }

}
```

1. 객체 termObj에 약관 정보를 저장했다. 객체를 사용한 것은 해쉬를 이용하여 배열 순회보다 안정적인 시간복잡도를 가지기 위해서이다.

2. 이후 배열을 순회하면서 각 데이터를 보낸다.

3. 연월일을 비교하여 return한 값들 중 true를 모아서 반환한다.

 

### **남의 풀이**

```
function solution(today, terms, privacies) {
  var answer = [];
  var [year, month, date] = today.split(".").map(Number);
  var todates = year * 12 * 28 + month * 28 + date;
  var t = {};
  terms.forEach((e) => {
    let [a, b] = e.split(" ");
    t[a] = Number(b);
  });
  privacies.forEach((e, i) => {
    var [day, term] = e.split(" ");
    day = day.split(".").map(Number);
    var dates = day[0] * 12 * 28 + day[1] * 28 + day[2] + t[term] * 28;
    if (dates <= todates) answer.push(i + 1);
  });
  return answer;
}
```

\- 나랑 동일한 로직이나 forEach 함수로 더 깔끔하게 구현하셨다.

\- 해당 문제에서 나는 마지막에 비교로직이 매우 긴데, 저렇게 숫자형태로 바꿔서 정량적으로 비교하면 생각보다 편하다.

예전에 초단위로 가는 문제여서 년월일분초 를 풀었는데 위에서는 if문이 많아서 실수를 한 적이 있는데, 이 방법을 사용해봐야겠다.

 

### **후기**

**-** 너무 느리다. 카카오 문제 예전에도 풀어봤는데, 이 문제에 한 시간 반을 사용하니 7문제를 다 풀 수가 없다.

\- 쉽지만 아직 함수가 익숙하지 않다. 어서 빨리 바꿔야겠다..