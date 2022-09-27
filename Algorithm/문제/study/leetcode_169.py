class Solution(object):
    def majorityElement(self, nums):
        set_nums = set(nums)
        for num in set_nums:
            temp_cnt = nums.count(num)
            if temp_cnt >= (len(nums)/2+1):
                return num