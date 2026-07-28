class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Map, s2Map = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Map[ord(s1[i]) - ord('a')] += 1 
            s2Map[ord(s2[i]) - ord('a')] += 1
        
        l = 0
        k = len(s1)
        while l + k < len(s2):
            if tuple(s1Map) == tuple(s2Map):
                return True
            s2Map[ord(s2[l]) - ord('a')]-=1
            s2Map[ord(s2[l + k]) - ord('a')] += 1
            l+=1
        return tuple(s1Map) == tuple(s2Map)