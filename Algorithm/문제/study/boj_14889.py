import sys
from itertools import combinations,permutations
sys.stdin = open("input.txt","r")

n = int(input())
statuses = []
for i in range(n):
    temp_status = list(map(int,input().split( )))
    statuses.append(temp_status)

members = []
members_num = int(n/2)
for i in range(n):
    members.append(i)
all_comb = list(combinations(members,members_num))
minimum_value = 99999999

for i in range(int(len(all_comb)/2)):
    first_team = all_comb[i]
    second_team = all_comb[-(i+1)]
    first_team_permu = list(permutations(first_team,2))
    second_team_permu = list(permutations(second_team,2))
    score = 0
    for j in range(len(first_team_permu)):
        score += statuses[first_team_permu[j][0]][first_team_permu[j][1]]
    for j in range(len(second_team_permu)):
        score -= statuses[second_team_permu[j][0]][second_team_permu[j][1]]
    if abs(score) < minimum_value:
        minimum_value = abs(score)
print(minimum_value)