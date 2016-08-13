# Given an amount of money and a list of coin values, return the least number of coins required to add up to the total.
# Also known as the knapsack problem
# Author: J. Plasmier | jplasmeier@gmail.com
# MIT License

def make_change(total, coins, count=None):
    # first call
    if count is None:
        count = 0
    # base case
    if total in coins:
        return count + 1
    for coin in reversed(sorted(coins)):
        if coin < total and total-coin > 0:
            print coin, total-coin
            return make_change(total-coin, coins, count + 1)
    

# Dynamic Programming Solution
def make_change_dp(total, coins, change=None, cache=None):
    # first call
    if change is None:
        change = []
    if cache is None:
        cache = {}
    # base case
    if total in coins:
        change.append(total)
        return change
    for coin in reversed(sorted(coins)):
        print cache
        if total in cache:
            print 'we hit the cache, isn\'t DP cool??'
            return change.extend(cache[total])
        if coin < total and total-coin > 0:
            change.append(coin)
            cache[sum(change)] = change
            return make_change_dp(total-coin, coins, change)
# this needs fixing during recursive data structures day 

total = 100
coins = [1,3,5,17]
print make_change_dp(total, coins)

total = 123
coins = [1,4,8,17,21]
print make_change_dp(total, coins)

total = 120
coins = [5,10]
print make_change_dp(total, coins)
