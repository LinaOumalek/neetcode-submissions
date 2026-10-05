class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        k = len(s1)
        count1= {}
        count2 = {}
        for i in s1:
            if i not in count1:
                count1[i] = 0
            count1[i] +=1

        for i in s2[:k]:
            if i not in count2:
                count2[i] = 0
            count2[i] +=1
        if count1 == count2:
            return True

        for i in range(len(s2) - k):
            count2[s2[i]] -= 1
            if count2[s2[i]] == 0:
                del count2[s2[i]]
            if s2[i+k] not in count2:
                 count2[s2[i+k]] = 0
            count2[s2[i+k]] += 1
            
            if count1 == count2:
                return True
        
        return False