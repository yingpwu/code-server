
from pprint import pprint as print


c = 10
w = [3, 4, 5, 7]
v = [1, 5, 6, 9]
n1 = [3, 4, 1, 2]
dp = [[0 for i in range(c+1)] for j in range(len(v)+1)]
w.insert(0, 0)
v.insert(0, 0)
print(dp)
for i in range(1, len(v)):
    for j in range(1, c+1):

        if w[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i][j-w[i]]+v[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp)

# 背包找路径


def get_path(dp, w, c):
    i = len(w)-1
    j = c
    res = []
    while i != 0 and c != 0:
        if dp[i][j-1] == dp[i-1][j-1]:
            i -= 1
        else:
            res.append(i-1)
            j -= w[i-1]
    print(res)


get_path(dp, w, c)
