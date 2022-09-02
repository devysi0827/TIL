import sys
sys.stdin=open("input.txt","r")

n, s = map(int,input().split())
seq = list(map(int,input().split()))

check_box = [0 for _ in range(len(seq))]
cnt = 0
def dfs(count,sum):
    global cnt
    if count == len(seq):
        if sum == s:
            cnt +=1
        return
    dfs(count+1,sum)
    sum += seq[count]
    dfs(count+1,sum)
dfs(0,0)
if s == 0 :
    print(cnt-1)
else:
    print(cnt)



