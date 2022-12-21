def groupAnagrams(self, strs):
    answer = []
    d = {}

    for i in range(len(strs)):
        word = ''.join(sorted(strs[i]))
        if word in d:
            d[word].append(strs[i])
        else:
            d[word] = [strs[i]]

    for (key, value) in d.items():
        answer.append(value)
    return answer

    # return d.values()