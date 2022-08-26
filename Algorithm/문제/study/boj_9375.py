import sys
sys.stdin = open("input.txt","r")


tc_num = int(input())
for tc in range(tc_num):
    closet = {}
    cloth_types = []
    clothes_num = int(input())

    for i in range(clothes_num):
        cloth, cloth_type = input().split()
        if cloth_type in cloth_types:
            temp_num = closet[cloth_type]
            closet[cloth_type] = temp_num + 1
        else:
            closet[cloth_type] = 1
            cloth_types.append(cloth_type)

    answer = 1
    for (key,value) in closet.items():
        answer *= (value+1)
    print(answer  - 1 )
