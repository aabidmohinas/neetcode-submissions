class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Numbers = set(nums)
        Long = 0
        
        for i in Numbers:
            if i - 1 not in Numbers:
                Length = 1
                while i + Length in Numbers:
                    Length += 1
                
                Long = max(Long, Length)

        return Long