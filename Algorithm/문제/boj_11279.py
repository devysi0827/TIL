import sys


#code1
from heapq import heappush, heappop
total_operation = int(input())
numbers = []
for i in range(total_operation):
    operation = int(sys.stdin.readline())
    if operation == 0:
        if len(numbers) == 0:
            print(0)
        else:
            print(heappop(numbers)[1])
    else:
        heappush(numbers,(-1*operation,operation))


#code 2

total_operation = int(input())
numbers = []
for i in range(total_operation):
    operation = int(sys.stdin.readline())
    if operation == 0:
        if len(numbers) == 0:
            print(0)
        else:
            print(numbers.pop())
    else:
        numbers.append(operation)


