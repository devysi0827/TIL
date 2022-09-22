class Solution(object):
    def letterCombinations(self, digits):
        alpabet = [
            ["a","b","c"],
            ["d","e","f"],
            ["g","h","i"],
            ["j","k","l"],
            ["m","n","o"],
            ["p","q","r","s"],
            ["t","u","v"],
            ["w","x","y","z"]
        ]
        n = len(digits)
        answer = []
        def three_bits(word):
            order = len(word)
            if order == n:
                answer.append(word)
            else:
                now = int(digits[order]) -2
                for i in range(len(alpabet[now])):
                    new_word = word
                    new_word += alpabet[now][i]
                    three_bits(new_word)
        three_bits("")
        if answer == [""]:
            return []
        else:
            return answer