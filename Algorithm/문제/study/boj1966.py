from collections import deque

repeat_num = int(input())

for repeat in range(repeat_num):
    docu_cnt, selected_num = map(int, input().split())
    docu_list = list(map(int, input().split()))
    q = deque()
    for i in range(len(docu_list)):
        if i == selected_num:
            q.append([docu_list[i],1])
        else:
            q.append([docu_list[i],0])
    print_flag = 0
    print_cnt = 0
    print("check")
    while print_flag == 0:
        print("while in")
        important_docu = max(q)
        for i in range(len(q)):
            if q[i][0] == important_docu[0]:
                if q[i][1] == 1:
                    print(print_cnt)
                    break
                else :
                    q[i][0] = -1
                    print_cnt += 1
                    popData = q.popleft()
                    q.append(popData)
            else:
                popData = q.popleft()
                q.append(popData)




