class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = [[] for _ in range(len(nums) +1)]
        res = []
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for num in freq:
            buckets[freq[num]].append(num)
        
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res
        

        