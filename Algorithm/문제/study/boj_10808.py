import sys
sys.stdin = open("input.txt","r")

word = input()
alpa_number_list = [0 for _ in range(26)]
for i in range(len(word)):
    alpa = ord(word[i])
    alpa_number_list[alpa-97] += 1

# for num in range(len(alpa_number_list)):
#     if num == len(alpa_number_list):
#         print(alpa_number_list[num])
#     else:
#         print(alpa_number_list[num],end=" ")
print(*alpa_number_list)