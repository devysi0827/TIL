import sys
from itertools import combinations, permutations
sys.stdin = open("input.txt","r")

house_num = int(input())
house_costs = []
for i in range(house_num):
    house_costs.append(list(map(int,input().split( ))))
dp_list = []
last_color = -1
last_colors = []
min_cost = 9999

# first
for i in range(3):
    if i != last_color and house_costs[0][i] < min_cost:
        min_cost = house_costs[0][i]
        last_color = i
dp_list.append(min_cost)
last_colors.append(last_color)

# second
# min_cost = 9999
# last_color = last_colors[-1]
# for i in range(3):
#     if i != last_color and house_costs[1][i]+dp_list[-1] < min_cost:
#         min_cost = house_costs[1][i]+dp_list[-1]
#         last_color = i
# dp_list.append(min_cost)
# last_colors.append(last_color)
abc = [1,2,3]
min_cost = 9999
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        else:
            if house_costs[0][i] + house_costs[1][j] < min_cost:
                min_cost = house_costs[0][i] + house_costs[1][j]
                last_color = j
dp_list.append(min_cost)
last_colors.append(last_color)

for i in range(2,house_num):
    min_cost = 9999
    last_color = last_colors[-1]
    for j in range(3):
        if j != last_color and house_costs[i][j] + dp_list[-1] < min_cost:
            min_cost = house_costs[i][j] + dp_list[-1]
            last_color = j

    for j in range(3):
        if j == last_colors[-1] and j == last_colors[-2]:
            continue
        last_color = j
    temp_value = house_costs[i-1][last_color] +dp_list[-2]

    for j in range(3):
        if j != last_color and house_costs[i][j] + temp_value < min_cost:
            min_cost = house_costs[i][j] + temp_value
            last_color = j
    dp_list.append(min_cost)
    last_colors.append(last_color)
print(dp_list[-1])







