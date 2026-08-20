class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                graph[pattern].append(word)
        
        q, visited = deque([beginWord]), set()
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word in visited:
                    continue
                visited.add(word)
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for nei in graph[pattern]:
                        q.append(nei)
            res += 1

        return 0