import sys
sys.stdin=open("input.txt","r")
# from collections import deque
#
# X = int(input())
# q = deque()
# q.append([X,0])
# ans= -1
#
# while q:
#     temp_number = q.popleft()
#     if temp_number[0] == 1:
#         ans = temp_number[1]
#         break
#
#     if temp_number[0] % 3 == 0:
#         q.append([temp_number[0]//3,temp_number[1]+1])
#     if temp_number[0] % 2 == 0:
#         q.append([temp_number[0] //2, temp_number[1] + 1])
#     q.append([temp_number[0] - 1, temp_number[1] + 1])
#
# print(ans)

from collections import deque
n = int(input())
queue = deque([(n, 0)])


while queue:
    num, cnt = queue.popleft()

    if num == 1:
        print(cnt)
        break
    if num % 3 == 0:
        queue.append((num // 3, cnt + 1))
    if num % 2 == 0:
        queue.append((num // 2, cnt + 1))
    queue.append((num - 1, cnt + 1))