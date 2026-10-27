class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append([value, timestamp])
        else:
            self.dic[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        l, r = 0, len(self.dic[key]) -1
        res = "" 
        k = float("-inf")
        while l <= r:
            mid = (l+r) // 2
            ts = self.dic[key][mid][1]
            if ts == timestamp:
                return self.dic[key][mid][0]
            if ts > timestamp:
                r = mid - 1
            elif ts < timestamp:
                if ts > k:
                    k = ts
                    res = self.dic[key][mid][0]
                l = mid +1 

        return res
