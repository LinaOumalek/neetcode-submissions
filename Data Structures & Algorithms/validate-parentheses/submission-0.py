class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for par in s:
            if par in ["(", "{", "["]:
                stack.append(par)
            else:
                if not stack or stack.pop() != mapping[par]:
                    return False
        return True if not stack else False