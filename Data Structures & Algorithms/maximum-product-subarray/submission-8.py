class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmin = cmax= global_max = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                cmin,cmax= cmax, cmin
            cmin = min(nums[i], cmin*nums[i])
            cmax = max(nums[i], cmax*nums[i])

            global_max = max(global_max, cmax)
        return global_max
