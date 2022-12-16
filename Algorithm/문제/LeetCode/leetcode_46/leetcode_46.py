class Solution(object):
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