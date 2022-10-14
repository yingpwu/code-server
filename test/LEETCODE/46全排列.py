# 回溯算法


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        visited = [0 for _ in range(len(nums))]

        def dfs(visited, path, depth, res):
            if depth == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if visited[i] == 0:
                    path.append(nums[i])
                    visited[i] = 1
                    dfs(visited, path, depth+1, res)
                    visited[i] = 0
                    path.pop()
        res = []
        dfs(visited=visited, path=[], depth=0, res=res)
        return res


# print(Solution().permute([1, 2, 3]))


