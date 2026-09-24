class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1= {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in hash1:
                return [hash1[x], i]
            hash1[nums[i]] = i
        