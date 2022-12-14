# **[python] Leetcode 34. Find First and Last Position of Element in Sorted Array**

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/



#### 문제 소개

- target과 동일한 숫자가 nums 배열안에 있다면, 그 숫자의 시작과 끝 index를 반환, 없다면 [-1,-1]를 반환하는 문제

- O(log n)의 시간복잡도 제한이 걸려있다. (정답은 시간제한을 일부 통과해도 되는 거 같다.)

- binary search(이진 탐색) 알고리즘을 사용한다.

  

#### Binary Search Code

```
class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1,-1]
        start = 0
        end = len(nums) -1

        while start < end:
            mid = int((start+ end)//2)

            if nums[mid] == target:
                start = mid
                end = mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid

        if start == end and nums[start] != target:
            return [-1,-1]

        for i in range(start,-1,-1):
            if nums[i] == target:
                start = i
            else:
                break
        
        for i in range(end,len(nums)):
            if nums[i] == target:
                end = i
            else:
                break
        
        
    
        return [start,end]
```

- 정석적인 이진탐색 코드를 사용하여 O(log n)을 만족하였습니다.
- **if not nums** 은 빈 nums에 대한 예외처리를 진행합니다.
- target이 만약 없을 경우, while문 이후 중앙으로 수렴합니다. 이 때, start== end이고 nums[start] != target이라면 값이 없는 것이므로 [-1,-1]을 반환하도록 코드를 작성했습니다. 