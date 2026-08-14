class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for c in s:
            if c.isalnum():
                new_s += c.lower()

        l = 0
        r = len(new_s) - 1
        while l <= r:
            if new_s[l] == new_s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True