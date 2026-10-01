class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*(len(temperatures))
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                j = stack[-1][0]
                res[j] = i - j
                stack.pop()
            stack.append([i, temp])
        return res