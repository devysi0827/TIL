import sys
sys.stdin = open("input.txt","r")

total_inequality= int(input())
inequality_list = list(input().split())

min_ans = 9999999999
max_ans = 0

def inequality_dfs(accumulted_number_list,index):
    global min_ans, max_ans
    if index == total_inequality + 1:
        accumulted_number = 0
        for i in range(len(accumulted_number_list)):
            accumulted_number = accumulted_number *10 + accumulted_number_list[i]
        if accumulted_number > max_ans:
            max_ans = accumulted_number
        if accumulted_number < min_ans:
            min_ans = accumulted_number
        return

    selected_inequality_sign = inequality_list[index-1]
    last_number = accumulted_number_list[-1]

    if selected_inequality_sign == '<':
        for i in range(10):
            if i > last_number and i not in accumulted_number_list :
                new_accumulted_number_list = list(accumulted_number_list)
                new_accumulted_number_list.append(i)
                inequality_dfs(new_accumulted_number_list,index+1)

    else :
        for i in range(10):
            if i < last_number and i not in accumulted_number_list :
                new_accumulted_number_list = list(accumulted_number_list)
                new_accumulted_number_list.append(i)
                inequality_dfs(new_accumulted_number_list,index+1)


for i in range(10):
    accumulted_number_list = []
    accumulted_number_list.append(i)
    inequality_dfs(accumulted_number_list,1)

k = [1,2,3]

min_ans = str(min_ans)
max_ans = str(max_ans)
if len(min_ans) < len(max_ans):
    min_ans = '0' + min_ans
print(max_ans)
print(min_ans)
