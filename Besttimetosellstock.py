def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Keep track of minimum buying price
        if price < min_price:
            min_price = price
        # Calculate profit if sold today
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


# Taking user input
n = int(input("Enter number of days: "))
prices = list(map(int, input("Enter stock prices separated by space: ").split()))

profit = maxProfit(prices)
print("Maximum Profit:", profit)