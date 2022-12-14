def letterCombinations(self, digits):
    if not digits:
        return []

        answer = []
    alpabet = [
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"],
        ["j", "k", "l"],
        ["m", "n", "o"],
        ["p", "q", "r", "s"],
        ["t", "u", "v"],
        ["w", "x", "y", "z"]
    ]

    def three_bits(word):
        if len(word) == len(digits):
            answer.append(word)
        else:
            now = int(digits[len(word)]) - 2
            for i in range(len(alpabet[now])):
                three_bits(word + alpabet[now][i])

    three_bits("")

    return answer