class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Nums = nums
        ReversedNums = Nums[::-1]
        Prefix = []
        Postfix = []
        Output = []
        for i in range(len(Nums)):
            if i == 0:
                Prefix.append(Nums[0])
                Postfix.append(ReversedNums[0])
            else:
                Product = Prefix[i - 1] * Nums[i]
                ReversedProduct = Postfix[i - 1] * ReversedNums[i]
                Prefix.append(Product)
                Postfix.append(ReversedProduct)
                Nums[i] = Product 
                ReversedNums[i] = ReversedProduct

        Postfix = Postfix[::-1] + [1]
        Prefix = [1] + Prefix

        for i in range(len(Nums)):
            Product = Prefix[i] * Postfix[i + 1]
            Output.append(Product)
            
        return Output