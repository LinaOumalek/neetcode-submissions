class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        gmax = 0
        mfrq = 0
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 0
            count[s[r]] += 1
            mfrq = max(mfrq, count[s[r]])
            while (r-l+1) - mfrq>k:
                count[s[l]]-= 1
                l += 1
                
            gmax = max(gmax, r-l+1)
        return gmax