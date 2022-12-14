# LeetCode_15

 ### 문제 소개

https://leetcode.com/problems/3sum/description/

- 주어진 배열에서 숫자 3개를 뽑고 그 합이 0인 배열리스트를 리턴하는 문제이다.
- 순열을 통해 완전 탐색을 할 경우 시간초과가 나온다.
- 투 포인터와 그리디 알고리즘을 사용한 두 가지 추천 코드를 들고 왔다.



### Two Pointer Code

```python
def threeSum(self, nums):
    nums.sort()
    answer = set()

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1] :
            continue
        left = i+1
        right = len(nums)-1

        while (left < right):
            sum = nums[i] + nums[left] +nums[right]

            if sum == 0 :
                answer.add((nums[i],nums[left],nums[right]))
                right -= 1
                left += 1
                while (left < right and nums[left] == nums[left-1]):
                    left +=1
                while (left < right and nums[right] == nums[right+1]):
                    right -=1
            elif (sum >0) :
                right -=1
            else :
                left +=1

    return map(list,answer)
```

- 변수가 세 가지이다
  - 반복문의 index에 속하는 원소
  - index + 1에 위치하는 원소(left)
  - len(nums)-1 에 위차하는 원소(right)
- 위 세 가지 중 index를 기준으로 left와 right 두 가지 포인터를 변경해가며 0이 되는 합을 찾는다.
  - 찾았다면, 그걸 기준으로 left, right를 변화해본다.
  - 정렬이 되어있기 때문에 sum이 양수면 right를 -1, 음수면 left를 +1한다.
- `if i > 0 and nums[i] == nums[i-1]` 이 부분은 없어도 되지만, 이 백트래킹으로 인해서 많은 시간적 이득을 볼 수 있다.



### Greedy Code

```python
def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        answer = set()
        for i in range(len(nums)-2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            x = nums[i]
            temp = {}
            for y in nums[i+1:]:
                if y not in temp:
                    temp[-x-y] = 1
                else:
                    answer.add((x,y,-x-y))

        return list(map(list,answer))
```

- `len()` 함수와 딕셔너리 관련 함수들은 O(1)의 시간복잡도를 가진다. 즉, 시간의 영향을 주지 않는다.

- x + y + z = 0 이므로 z = -x - y 이다.

- index1 = x, index2 = y 두가지를 순회하면서,  -x-y 랑 같은 값이 있다면 이 세 변수는 sum = 0이 된다.

  