class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for idx in nums:
            if nums[abs(idx)] < 0:
                return abs(idx)
            nums[abs(idx)] = - nums[abs(idx)]