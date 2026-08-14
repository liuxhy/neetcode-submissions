class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        window = set()
        res = 0

        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[start])
                start += 1
            window.add(s[i])
            res = max(res, i - start + 1)

        return res