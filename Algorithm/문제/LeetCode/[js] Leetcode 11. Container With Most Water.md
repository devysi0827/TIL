
# **[js] Leetcode 11. Container With Most Water**

### 문제

https://leetcode.com/problems/container-with-most-water/

서로 다른 높이의 벽이 나열되어 있다. 

두 개의 벽을 선택하여서 물을 담는다 하였을 때, 가장 많은 물을 담을 수 있는 양을 구하시오 (물의 양은 높이 x 길이)

 

### 아이디어

1. 너비를 양 끝으로 잡아서 최대 너비를 만들고, 작은 높이를 곱해서 기준 값을 구한다. (큰 높이는 물이 넘쳐서 의미가 없다.)

2. 여기서 너비를 하나 줄인다. 이 때, 당연히 둘 중 작은 높이를 가진 쪽을 줄인다.

3.  현재 너비 x min(높이1, 높이2)를 구하고 기준 값보다 크다면 기준값을 바꾼다.

4. 두 포인터가 같아질때까지 2-3을 반복한다.

 

### 구현(풀이)

```
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let s = 0
    let e = height.length-1
    let direction = (height[s] <= height[e]) ? 1 : -1
    let maxValue = (e-s) * Math.min(height[s],height[e])
    while (s < e) {
        if (direction > 0) {
            s +=1
        }
        else {
            e -= 1
        }
        direction = (height[s] <= height[e]) ? 1 : -1
        const value = (e-s) * Math.min(height[s],height[e])
        if (value > maxValue) {
            maxValue = value
        }
    }

    return maxValue
};
```

###  

### 남의 풀이

```
var maxArea = function(H) {
    let ans = 0, i = 0, j = H.length-1
    while (i < j) {
        ans = Math.max(ans, Math.min(H[i], H[j]) * (j - i))
        H[i] <= H[j] ? i++ : j--
    }
    return ans
};
```

같은 로직이다. 위처럼 깔끔하게 쓸 수 있어서 더 설명하지 않는다.

 