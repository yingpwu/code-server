
from pprint import pprint as print
from readline import insert_text


c = 10
w = [3, 4, 5, 7]
v = [1, 5, 6, 9]
n1 = [3, 4, 1, 2]
dp = [[0 for i in range(c+1)] for j in range(len(v)+1)]
w.insert(0, 0)
v.insert(0, 0)
n1.insert(0, 0)
# print(dp)

for i in range(1, len(v)):
    counter = [0 for i in range(c+1)]
    # 创建对于一个物体i的每个容量下的个数列表
    for j in range(1, c+1):

        if w[i] <= j:
            # 背包该物体是否能放下
            if counter[j-w[i]] < n1[i]:
                # 没有超过数量
                dp[i][j] = max(dp[i-1][j], dp[i][j-w[i]]+v[i])
                counter[j] = counter[j-w[i]]+0 if dp[i][j] == dp[i-1][j]else 1
            else:
                # 超过规定数量
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-n1[i]*w[i]]+n1[i]*v[i])
                counter[j] = n1[i]

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
