class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, integer in enumerate(nums):
            diff = target - integer
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[integer] = i