class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b)}
        stack = []
        for t in tokens:
            if t in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(ops[t](num1, num2))
            else:
                stack.append(int(t))
        return stack[-1]

