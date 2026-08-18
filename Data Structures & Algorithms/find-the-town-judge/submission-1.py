class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int)
        for a, b in trust:
            delta[b] += 1
            delta[a] -= 1
        
        for person in delta:
            if delta[person] == (n -1):
                return person
        return -1