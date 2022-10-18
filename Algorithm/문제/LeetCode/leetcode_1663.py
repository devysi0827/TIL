class Solution(object):
    def getSmallestString(self, n, k):
        z_num = ord("z") - ord("a") + 1
        answer = ""
        while n:
            n -= 1
            if k - n >= z_num:
                answer += "z"
                k -= z_num
            else:
                answer += chr(96 + k - n)
                k -= (k - n)
        return answer[::-1]
