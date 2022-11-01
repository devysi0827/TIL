class Solution(object):
    def maxLength(self, arr):
        global long_length
        long_length = -1

        def bits_calc(bits):
            global long_length
            if len(bits) == len(arr):
                answer_word = ""
                for i in range(len(bits)):
                    if bits[i] == '1':
                        answer_word += arr[i]
                        if len(answer_word) != len(set(answer_word)):
                            return
                if long_length < len(answer_word):
                    long_length = len(answer_word)
            else:
                new_bits = bits + "1"
                bits_calc(new_bits)
                new_bits = bits + "0"
                bits_calc(new_bits)

        bits_calc("")
        return long_length


