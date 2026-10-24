from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = Counter(nums)
        for key, value in hashmap.items():
            if value > 1:
                return True

        return False