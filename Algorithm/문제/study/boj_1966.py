import sys
sys.stdin = open("input.txt","r")

def print_selected_docu():
    global importance, print_cnt
    is_selected_docu = False

    while is_selected_docu == False:
        important_docu_value = -1
        important_docu_index = -1

        for i in range(importance,len(docu_list)):
            if docu_list[i] > important_docu_value:
                important_docu_value = docu_list[i]
                important_docu_index = i

        for i in range(importance):
            if docu_list[i] > important_docu_value:
                important_docu_value = docu_list[i]
                important_docu_index = i

        if important_docu_index == selected_num :
            is_selected_docu = True
        else:
            docu_list[important_docu_index] = -1
            print_cnt +=1
            importance = important_docu_index


test_case_num = int(input())
for test_case in range(test_case_num):
    docu_num, selected_num = map(int,input().split(' '))
    docu_list = list(map(int,input().split(' ')))
    importance = 0
    print_cnt = 1
    print_selected_docu()
    print(print_cnt)
