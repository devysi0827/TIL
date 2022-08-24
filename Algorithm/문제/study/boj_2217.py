import sys
sys.stdin = open("input.txt","r")

lope_num = int(input())
lopes = []
for i in range(lope_num):
    lopes.append(int(input()))

lopes.sort(reverse=True)
max_weight = 0
for i in range(len(lopes)):
    weight = lopes[i] *(i+1)
    if weight > max_weight:
        max_weight = weight
print(max_weight)
