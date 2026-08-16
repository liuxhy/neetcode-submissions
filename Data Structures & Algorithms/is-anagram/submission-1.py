class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1

        for c in t:
            if c in dic:
                dic[c] -= 1
            else:
                return False

        for num in dic.values():
            if num != 0:
                return False

        return True