def min_coins(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[target]

denominations = [1, 2, 5, 10, 25]
target_amount = 63
min_coins_needed = min_coins(denominations, target_amount)
print(min_coins_needed)