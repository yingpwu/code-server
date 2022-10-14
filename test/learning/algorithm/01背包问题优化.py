
from pprint import pprint as print


c = 10
w = [3, 2, 5, 7]
v = [1, 6, 6, 9]
dp = [0 for i in range(c+1)]
w.insert(0, 0)
v.insert(0, 0)
print(dp)
for i in range(1, len(v)):
    for j in range(c, 0, -1):
        if w[i] <= j:
            dp[j] = max(dp[j], dp[j-w[i]]+v[i])
        # print(dp)
print(dp)
