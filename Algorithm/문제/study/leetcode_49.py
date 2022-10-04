def groupAnagrams(strs):
    answer_dict = {}
    for i in range(len(strs)):
        word = sorted(strs[i])
        str = ""
        for alpa in word:
            str += alpa
        if str in answer_dict:
            answer_dict[str].append(strs[i])
        else:
            answer_dict[str] = []
            answer_dict[str].append(strs[i])
    return answer_dict

strs = ["eat","tea","tan","ate","nat","bat"]

answer_dict = groupAnagrams(strs)
answer = []
for (key,value) in answer_dict.items():
    answer.append(value)
print(answer)