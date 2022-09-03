prices = [7,1,5,3,6,4]


def maxProfit(prices):
    profit = 0
    min_price = prices[0]

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            if (prices[i] - min_price) > profit:
                proift = prices[i] - min_price

    return profit

print(maxProfit(prices))

