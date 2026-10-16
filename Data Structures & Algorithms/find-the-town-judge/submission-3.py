class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mp = defaultdict(int)

        for a, b in trust:
            mp[b] += 1
            mp[a] -= 1

        for person in mp:
            if mp[person] == n - 1:
                return person
        return -1
