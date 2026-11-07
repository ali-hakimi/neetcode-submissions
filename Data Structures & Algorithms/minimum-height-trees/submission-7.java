class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) {
            return new ArrayList<>(List.of(0));
        }
        Map<Integer, Set<Integer>> edgeCount = new HashMap<>();
        for (int[] edge : edges) {
            int n1 = edge[0], n2 = edge[1];
            edgeCount.computeIfAbsent(n1, k -> new HashSet<>()).add(n2);
            edgeCount.computeIfAbsent(n2, k -> new HashSet<>()).add(n1);
        }

        Queue<Integer> queue = new LinkedList<>();

        for (int node : edgeCount.keySet()) {
            if (edgeCount.get(node).size() == 1) {
                queue.offer(node);
            }
        }

        int remaining = n;
        while (remaining > 2) {
            int queueSize = queue.size();
            for (int i = 0; i < queueSize; i++) {
                int node = queue.poll();
                int nei = edgeCount.get(node).iterator().next();
                edgeCount.remove(node);
                edgeCount.get(nei).remove(node);
                if (edgeCount.get(nei).size() == 1) {
                    queue.offer(nei);
                }
                remaining--;
            }
        }
        if (remaining == 2) {
            return new ArrayList<>(List.of(queue.poll(), queue.poll()));
        }
        return new ArrayList<>(List.of(queue.poll()));
    }
}