import sys
sys.stdin = open("input.txt","r")
import math

n = int(input())
budgets = list(map(int,input().split( )))
total_budget = int(input())

if sum(budgets) <= total_budget:
    print(max(budgets))
else:
    temp_budgets = []
    avg_budget = math.floor(total_budget / n)
    for budget in budgets:
        if avg_budget >= budget:
            temp_budgets.append(budget)
    max_budget = (math.floor((total_budget-sum(temp_budgets))/(n-len(temp_budgets))))

    while max_budget *(n-len(temp_budgets)) +sum(temp_budgets) <= total_budget:
        max_budget += 1
        temp_budgets = []
        for budget in budgets:
            if max_budget >= budget:
                temp_budgets.append(budget)

    print(max_budget-1)

