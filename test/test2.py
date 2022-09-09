# print(float("inf"))
from time import sleep


amount = 11
coins = [1, 2, 3, 4, 5]
dp = [float("inf")]*(amount+1)
dp[0] = 0
# print(dp)
# print(coins)
for i in range(1, amount+1):
    # for c in coins:
    #     if i-c >= 0:
    #         dpi = dp[i-c]
    #     else:
    #         dpi = float("inf")
    dpi = (dp[i-c] if i - c >= 0 else float("inf") for c in coins)
    for one in dpi:
        print(one)
    print("--------------------------")
    # dp[i]=min(dpi)+1
    # dp[i]=min(dp[i-c] if i -c >=0 else float("inf") for c in coins)+1
    # print(dp[i])
    # sleep(3)
# print(dp[-1])
