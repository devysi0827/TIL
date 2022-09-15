import sys
sys.stdin = open("input.txt","r")

n, k = map(int, input().split())
dolls = list(map(int, input().split()))
s = 0
e = 0
answer = int(1e9)
lion_num = 0

if dolls[0] == 1:
    lion_num +=1

while e < n:
    if lion_num >= k:
        if e-s+1 < answer:
            answer = e - s+1
        if dolls[s] == 1:
            lion_num -= 1
        s += 1

    else:
        e += 1
        if e < n and dolls[e] == 1:
            lion_num += 1


if answer == int(1e9):
    print(-1)
else:
    print(answer)