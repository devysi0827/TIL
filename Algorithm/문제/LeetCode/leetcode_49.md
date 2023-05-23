# **[python] **Leetcode 49. Group Anagrams

https://leetcode.com/problems/group-anagrams/

###  

### **문제 소개**

- 요약: 애나그램이 같은 문자열끼리 묶은 값 이중배열을 반환하시오
- 관련 토픽(알고리즘, 라이브러리) : sorting , Hash Table

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

###  

### **Code & 설명**

```python
def groupAnagrams(self,strs):
    answer = []
    d = {}

    for i in range(len(strs)):
        word = ''.join(sorted(strs[i]))
        if word in d:
            d[word].append(strs[i])
        else:
            d[word] = [strs[i]]

    for (key,value) in d.items():
        answer.append(value)
    return answer
    
    # return d.values()
```

- **word = ''.join(sorted(strs[i]))** 을 통해서 각 단어를 정렬 후 문자열로 생성했다.
- 이후 딕셔너리 안에 word가 존재한다면 기존 값에 append 없다면 생성한다.
- 딕셔너리를 순회하며 value값을 배열에 넣고 반환한다.
- 마지막 세 줄을 **d.values()** 로 표현할 수 있다.