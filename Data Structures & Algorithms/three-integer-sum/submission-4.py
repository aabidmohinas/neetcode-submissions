class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def TwoSum(
            Numbers: list, Complement:  int
            ) -> list[int]:

            Left = 0
            Right = len(Numbers) - 1
            Output = []

            while Left < Right:
                CurrentSum = Numbers[Left] + Numbers[Right] + Complement
                SubArray = [Complement, Numbers[Left], Numbers[Right]]
                if CurrentSum == 0:
                    Output.append(SubArray)
                    Left += 1
                    Right -= 1
                    
                    while Left < Right and Numbers[Left] == Numbers[Left - 1]:
                        Left += 1
                    while Left < Right and Numbers[Right] == Numbers[Right + 1]:
                        Right -= 1
                    
                elif CurrentSum < 0:
                    Left += 1
                elif CurrentSum > 0:
                    Right -= 1

            return Output
        
        Output = []
        for i in range(len(nums)):
            SubArray = TwoSum(
                nums[i + 1:], nums[i] 
            )
            if not SubArray or nums[i] == nums[i - 1] and i > 0:
                continue
            else:
                Output.extend(SubArray)

        return Output
                
                    