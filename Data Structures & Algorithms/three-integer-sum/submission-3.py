class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if (i-1 >= 0) and nums[i] == nums[i-1]:
                continue
            p1, p2= i+1, len(nums)-1
            while p1 < p2:
                s= nums[i] + nums[p1] + nums[p2]
                if s == 0:
                    res.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    while p1 < p2 and nums[p1] == nums[p1 - 1]:
                        p1 += 1

                    while p1 < p2 and nums[p2] == nums[p2 + 1]:
                        p2 -= 1
                elif s > 0:
                    p2 -= 1
                elif s<0:
                    p1 += 1
        return res
