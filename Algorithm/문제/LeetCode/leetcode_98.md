# **[python] Leetcode 98. Validate Binary Search Tree**

https://leetcode.com/problems/validate-binary-search-tree/description/



### **문제 소개**

- 요약 : 해당 함수가 BST(이진 탐색 트리)가 맞는 지 확인하는 문제다
- 관련 토픽 : DFS, BST

### **BST**

- 이진 탐색 트리는 현재 노드와 비교하여 왼쪽에는 작은 값의 노드가, 오른쪽에는 큰 값의 노드가 존재하는 트리를 의미한다.
- python은 타 언어와 다르게 공식 Tree Library가 없다. 그래서 Leetcode에서 직접 구현된 Tree 함수 기능을 사용해야한다.
  - 왜인지 조사했는데, 공식적인 이유는 밝혀진 게 없다.
  - 사람들의 추측상 python의 설계원칙(Explicit is better than implicit.)에 따라서 포인터를 사용하지 않는 것 같다. 트리 또한 포인터를 사용하여서, 트리를 공식적으로 작성하지 않은 것으로 추측한다.
  - 파이썬이 트리(포인터)를 사용하지 않는 이유 : https://realpython.com/pointers-in-python/#why-doesnt-python-have-pointers
  - 파이선 설계원칙 :https://peps.python.org/pep-0020/#id3

 

### **Code & 설명**

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        global ans
        ans = True
        def dfs(node, left_min, right_max):
            global ans
            print(node.val,left_min,right_max)
            if node :
                if (node.val >= right_max) :
                    ans = False
                    return
                if (node.val <= left_min):
                    ans = False
                    return
            if node.left : dfs(node.left, left_min, node.val)
            if node.right : dfs(node.right, node.val, right_max)
    
        dfs(root,-pow(2,31)-1,pow(2,31)+1)
        return ans
```

- 정석적인 BST 코드를 사용한다. 

  

  - max, min, val 세 개를 이용하여 현재 노드 값이 존재해도 되는 지, 다음 노드의 상한선 또는 하한선을 바꿔가며 재귀적으로 검토했다.
  - 만약 왼쪽으로 간다면, 현재의 노드값이 최댓값이 되고, 오른쪽으로 간다면, 현재의 노드값이 최솟값이 된다.
  - 시작점은 각각 최대/최소 값으로 pow(2,31)과 -pow(2,31)+1 로 정했다. 애매하게 크게 잡았다가 테스트 케이트를 통과하지 못했다.