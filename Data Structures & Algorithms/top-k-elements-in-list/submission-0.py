class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = sorted(count.items(), key=lambda item:-item[1])
        res = []

        for num, freq in count:
            if k == 0:
                break

            res.append(num)
            k -= 1

        return res