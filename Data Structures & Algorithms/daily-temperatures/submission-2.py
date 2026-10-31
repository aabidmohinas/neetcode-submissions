class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        Output = []
        if len(set(temperatures)) == 1:
            return [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i,len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    Output.append(j - i)
                    break
            else:
                Output.append(0)
        return Output