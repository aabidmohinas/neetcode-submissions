class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            l, r = numbers[left], numbers[right]
            if l + r == target:
                return [left + 1, right + 1]
            if l + r > target:
                right -= 1
            else:
                left += 1