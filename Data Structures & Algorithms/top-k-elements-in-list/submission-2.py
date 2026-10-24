from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [(0,0)] * 2001
        res = []
        for num in nums:
            if bucket[num + 1000] == (0,0):
                bucket[num + 1000] = [num, 1]
            else:
                bucket[num + 1000][1] += 1

        for i in range(k):
            v = max(bucket, key = lambda x: x[1])
            val , c = v
            res.append(val)
            bucket.remove(v)
        
        return res
