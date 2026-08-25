class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp[i] = true means the last index is reachable from index i
        n = len(nums)
        dp = [False] * n
        print(dp)
        dp[-1] = True
        for i in range(n - 2, -1, -1):
            end = min(n, i + nums[i] + 1)
            for j in range(i+1, end):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]
