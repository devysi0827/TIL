import sys
sys.stdin = open("input.txt","r")

n = int(input())
for i in range(n):
    x,y = list(map(int,input().split()))
    result = pow(x,y,10)
    if result:
        print(result)
    else:
        print(10)