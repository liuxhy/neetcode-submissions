class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)       
        res = 0
        for num in nums_set:
            current_streak = 0
            k = num
            if k - 1 not in nums_set:
                while k in nums_set:
                    current_streak += 1
                    k += 1
                res = max(res, current_streak)
        return res