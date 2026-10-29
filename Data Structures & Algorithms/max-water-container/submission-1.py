class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mArea = -float('inf')
        
        Left = 0
        Right = len(heights) - 1

        def Area(l, r, h):
            return (r - l) * h

        while Left < Right:
            Base = Right - Left
            Height = min(heights[Left], heights[Right])
            mArea = max(mArea, Area(Left, Right, Height))

            if heights[Left] > heights[Right]:
                Right -= 1
            elif heights[Left] < heights[Right]:
                Left += 1
            else:
                Right -= 1
                Left += 1

        return mArea
            