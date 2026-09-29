class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        gmax= 0
        for num in nums:
            if num - 1 not in set1:
                c_max = 1
                while num + 1 in set1:
                    c_max += 1
                    num = num + 1
                gmax = max(gmax, c_max)
        return gmax