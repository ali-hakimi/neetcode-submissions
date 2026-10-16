class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1 :])
                digit = str((int(lock[i]) + 9) % 10)
                res.append(lock[:i] + digit + lock[i + 1 :])
            return res

        turn = 0
        q = deque(["0000"])
        deadends.append("0000")
        deadends = set(deadends)

        while q:
            for _ in range(len(q)):
                lock = q.popleft()
                if lock == target:
                    return turn

                for child in children(lock):
                    if child in deadends:
                        continue
                    deadends.add(child)
                    q.append(child)
            turn +=1
        return -1
