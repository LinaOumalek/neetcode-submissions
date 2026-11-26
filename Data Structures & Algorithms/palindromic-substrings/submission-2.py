class Solution:
    def countSubstrings(self, s: str) -> int:
        self.c = 0
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                self.c += 1



        for i in range(len(s)):

            # odd length palindrome
            p1 = expand(i, i)

            # even length palindrome
            p2 = expand(i, i + 1)


        return self.c
