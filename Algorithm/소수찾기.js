function solution(numbers) {
    
    const maxNumber = Number(numbers.split('').sort((a,b) => b-a).join(''))
    const oddDp = Array.from({length : maxNumber +1}).fill(0)
    
    function makeOddTable() {
        for (let i =2; i< Math.sqrt(maxNumber); i++) {
            if (oddDp[i] === 0) {
                for (let j = i*2; j < maxNumber; j+=i){
                    if(oddDp[j] ===0) {
                        oddDp[j] = 1    
                    }  
                }
            }
        }
    }

    makeOddTable()
    
    function checkOdd(x) {
        if (oddDp[x] === 0) {
            return true
        } 
        return false
    }
    
    // 소수 체크
    
    var answers = [];
    
    function permute(arr, m = []) {
        if (arr.length === 0 && checkOdd(m)) {
            answers.push(parseInt(m.join(''), 10)); // 배열을 숫자로 변환하여 추가
        } else {
            for (let i = 0; i < arr.length; i++) {
                const current = arr.slice(); // 배열 복사
                const next = current.splice(i, 1); // 현재 요소를 제거
                permute(current, m.concat(next)); // 재귀 호출로 다음 순열을 생성
            }
        }
    }
    
    permute(numbers.toString().split(''))

    
    return Array.from(new Set(answers)).length;
}

solution('17')