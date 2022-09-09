
from pprint import pprint as print


c = 10
w = [3, 4, 5, 7]
v = [1, 5, 6, 9]
n1 = [3, 4, 1, 2]
dp = [[0 for i in range(c+1)] for j in range(len(v)+1)]
w.insert(0, 0)
v.insert(0, 0)
# print(dp)

for i in range(1, len(w)):
    for j in range(1, c+1):
        if w[i] <= j:
            k = j//w[i]
            k = n1[i-1] if k > n1[i-1] else k
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-k*w[i]]+k*v[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp)
