import sys
sys.stdin = open("input.txt","r")

n, k = list(map(int, input().split()))
numbers = [i+1 for i in range(n)]
point = -1
answer = []

while numbers:
    point += k
    if point >= len(numbers):
        point %= len(numbers)
    answer.append(str(numbers[point]))
    numbers.pop(point)
    point -=1

print("<",', '.join(answer),">", sep="")



