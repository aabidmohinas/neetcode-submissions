from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        c = Counter(nums)
        return sorted(c, key = c.get)[::-1][:k]