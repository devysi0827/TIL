class Solution(object):
    def topKFrequent(self, nums, k):
        number_dic = {}
        for i in nums:
            if i in number_dic:
                number_dic[i] += 1
            else:
                number_dic[i] = 1

        sorted_dict = sorted(number_dic.items(), key = lambda item: item[1], reverse = True)

        ans = []
        for i in range(k):
            ans.append(sorted_dict[i][0])

        return ans