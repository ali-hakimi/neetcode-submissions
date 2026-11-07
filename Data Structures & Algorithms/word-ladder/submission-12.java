class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (!wordList.contains(endWord)) {
            return 0;
        }

        Map<String, Set<String>> graph = new HashMap<>();

        for (String word: wordList) {
            for (int i = 0; i < word.length(); i++) {
                String pattern = word.substring(0, i) + "*" + word.substring(i + 1, word.length());
                graph.computeIfAbsent(pattern, k -> new HashSet<>()).add(word);
            }
        }
        
        int ladderLen = 1;
        Queue<String> q = new LinkedList<>();
        q.offer(beginWord);
        while (!q.isEmpty()) {
            int qSize = q.size();
            for (int i = 0; i < qSize; i++) {
                String word = q.poll();
                if (word.equals(endWord)) {
                    return ladderLen;
                }
                for (int j = 0; j < word.length(); j++) {
                    String pattern = word.substring(0, j) + "*" + word.substring(j + 1, word.length());
                    if (graph.containsKey(pattern)) {
                        for (String nei: graph.get(pattern)) {
                            q.offer(nei);
                        }
                        graph.remove(pattern);
                    }
                }
            }
            ladderLen++;
        }

        return 0;
    }
}
