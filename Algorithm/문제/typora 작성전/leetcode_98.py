class Solution(object):
    def isValidBST(self, root):
        global ans
        ans = True

        def dfs(node, left_min, right_max):
            global ans
            print(node.val, left_min, right_max)
            if node:
                # print("node : ", node.val, node.left.val, left_min, node.left.val <= left_min)
                if (node.val >= right_max):
                    ans = False
                    return
                if (node.val <= left_min):
                    ans = False
                    return
            if node.left: dfs(node.left, left_min, node.val)
            if node.right: dfs(node.right, node.val, right_max)

        dfs(root, -pow(2, 31) - 1, pow(2, 31) + 1)
        return ans