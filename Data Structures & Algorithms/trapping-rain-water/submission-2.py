class Solution:
    def trap(self, height: List[int]) -> int:
        leftm = []
        rheight = height[::-1]
        rightm = []

        lm = 0
        rm = 0

        for i in range(len(height)):

            lm = max(lm, height[i])
            leftm.append(lm)

            rm = max(rm, rheight[i])
            rightm.append(rm)
        
        rightm = rightm[::-1]

        output = [min(pairs) for pairs in list(zip(leftm, rightm))]
        for i,h in enumerate(height):
            output[i] -= h

        return sum([x for x in output if x > 0])
        
        