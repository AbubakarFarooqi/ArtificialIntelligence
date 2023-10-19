def max_profit_from_rod(length, prices, memo):
    if length == 0:
        return 0

    if memo[length] is not None:
        return memo[length]

    max_profit = -float("inf")
    for cut_length in range(length):
        max_profit = max(max_profit, prices[cut_length] + max_profit_from_rod(length - cut_length - 1, prices, memo))

    memo[length] = max_profit
    return max_profit

prices_per_length = [3, 5, 8, 9, 10, 17, 17, 20]
rod_length = 8
memoization_table = [None] * (rod_length + 1)
maximumValue = max_profit_from_rod(rod_length, prices_per_length, memoization_table)
print("The maximum value is", maximumValue)
