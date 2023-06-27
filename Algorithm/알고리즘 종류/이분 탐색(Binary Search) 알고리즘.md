# 이분 탐색(Binary Search) 알고리즘

### **이분탐색이란?**

\- 정렬되어 있는 리스트에서 탐색 범위를 반씩 줄이며 특정 원소를 찾는 탐색하는 알고리즘입니다. (정렬이 되어있지 않다면, 정렬해야합니다.)

\- 반씩 좁혀가며 탐색하므로 O(log n)의 시간 복잡도를 가집니다.

 

### **이분 탐색 구현**

```
function binarySearch(arr, target) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] === target) {
      return mid;
    } else if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1; // 찾는 값이 배열에 없을 경우
}
```

이분 탐색의 로직을 핵심 로직을 살펴보겠습니다.

1. 시작점과 끝점을 양 끝으로 설정합니다. 그리고 이 중앙에 해당하는 위치를 찾습니다.

2. 해당 중앙값을 기준으로 찾고자하는 값과 비교합니다. 만약 찾고자 하는 값이 크다면, 중앙-끝을, 작다면, 시작-중앙으로 범위를 좁히고 해당 로직을 지속적으로 반복합니다.

3. 만약, 찾고자하는 값과 같다면 해당 위치를 반환합니다. 모든 순회 결과 찾고자하는 값이 없다면(시작점이 끝점과 같거나 커진다면) -1을 반환합니다.