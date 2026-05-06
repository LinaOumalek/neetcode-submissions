class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.res = []

        def dfs(curr,idx):
            if idx == len(digits):
                if curr != "":
                    self.res.append(curr)
                return
            letters = digitToChar[digits[idx]]

            for letter in letters:
                dfs(curr + letter, idx +1)

        dfs("", 0)
        return self.res
        