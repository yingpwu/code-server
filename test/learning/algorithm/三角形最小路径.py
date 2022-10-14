import copy
from pprint import pprint


question = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3],
    [5, 7, 5, 3, 1]
]

# dp=[[0 for j in i] for i in question ]
# dp[0][0] = question[0][0]
dp = copy.deepcopy(question)
# print("问题", question)
# print(dp)
for i, listi in enumerate(question):
    if i == 0:
        continue
    else:
        for j, valuej in enumerate(listi):
            if j == 0:
                dp[i][j] = dp[i-1][j]+valuej
            elif i == j:
                dp[i][j] = dp[i-1][j-1]+valuej
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1])+valuej
print("最小值为", min(dp[len(question)-1]))
print("dp为", dp)


def get_path_index(dp, question) -> list:
    dp_copy = copy.deepcopy(dp)
    question_copy = copy.deepcopy(question)

    question_inverse = question_copy[::-1]
    dp_path = []

    min_index_last_dp = dp_copy[-1].index(min(dp_copy[-1]))

    min_value = min(dp_copy[-1])-question[-1][min_index_last_dp]
    dp_path.append(min_index_last_dp)
    for i, listi in enumerate(dp_copy[::-1]):
        if i == 0:
            continue
        min_index = listi.index(min_value)
        min_value -= question_inverse[i][min_index]
        dp_path.append(min_index)

    return dp_path[::-1]


print("路径索引为", get_path_index(dp, question))


def get_path(path_index: list) -> list:
    path = [question[index][i] for index, i in enumerate(path_index)]
    return path


print("选中数字为", get_path(get_path_index(dp, question)))
