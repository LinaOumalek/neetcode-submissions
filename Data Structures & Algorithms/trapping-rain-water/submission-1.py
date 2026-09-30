class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        rmaxes= [0] * len(height)
        lmaxes= [0] * len(height)
        lm = height[0]
        rm = height[len(height)-1]

        for i in range(1, len(height)):
            lmaxes[i] = lm
            if height[i] > lm:
                lm = height[i]
        
        for i in range(len(height)-2, -1,-1):
            rmaxes[i]= rm
            if height[i] > rm:
                rm = height[i]

        for i in range(1, len(height) -1):
            left_max = lmaxes[i]
            right_max = rmaxes[i]
            if min(left_max, right_max) <= height[i]:
                continue
            water = min(left_max, right_max) - height[i]
            res += water
        return res

            
