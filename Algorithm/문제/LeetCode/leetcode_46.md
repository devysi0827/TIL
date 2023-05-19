# **[python] Leetcode 46. Permutations**

https://leetcode.com/problems/permutations/



### **문제 소개**

- 요약: 숫자 배열에 대하여 모든 순열을 구하시오
- 관련 토픽(알고리즘, 라이브러리) : dfs

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

###  

### **Code & 설명**

```
def permute(self, nums):
        global ans
        ans = []

        def dfs(left_nums,permu):
            global ans
            if not left_nums:
                ans.append(permu)
                return
            else:
                for i in range(len(left_nums)):
                    dfs(left_nums[:i] + left_nums[i+1:],permu + [left_nums[i]])

        dfs(nums,[])
        return ans
```

- dfs를 이용하여 재귀적으로 숫자를 하나씩 리스트에 더해서 순열을 만들 수 있다.
  1. 숫자 하나( **left_nums[i]** )를 고른다
  2. 슬라이싱을 이용하여 해당 숫자를 제외한 배열을 만든다. ( left_nums[:i] + left_nums[i+1:] )
  3. 고른 숫자를 permu에 추가한다.
  4.  1-3을 반복하던 중 left_nums가 없다면, 순열이 완성된 것이므로 ans에 추가한 뒤 return(종료)한다.