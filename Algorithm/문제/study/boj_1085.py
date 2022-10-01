import sys
sys.stdin = open("input.txt","r")

x, y, w, h =list(map(int,input().split()))

print(min(x,y,w-x,h-y))