# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        q = deque()
        q.append(root)
        container = []

        while q:
            node = q.popleft()
            if node:
                container.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                container.append("null")

        level_length = 1
        cnt = 0
        answer = []
        level = []

        for i in range(len(container)):
            cnt += 1
            if container[i] != "null":
                level.append(container[i])

            if cnt == level_length:
                cnt = 0
                level_length = len(level) * 2
                if level:
                    answer.append(level)
                level = []

        return answer