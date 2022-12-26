class Solution(object):
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])
        # print(pairs)
        answer = 1
        last_number = -1
        for i in range(len(pairs)):
            if i == 0:
                last_number = pairs[0][1]
            else:
                if last_number < pairs[i][0]:
                    answer += 1
                    last_number = pairs[i][1]

        return answer
