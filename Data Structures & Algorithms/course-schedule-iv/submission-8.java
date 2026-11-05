class Solution {
    Map<Integer, Set<Integer>> adj = new HashMap<>();
    Map<Integer, Set<Integer>> graph = new HashMap<>();
    int[][] prerequisites;
    int[][] queries;
    List<Boolean> res = new ArrayList<>();
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        this.prerequisites = prerequisites;
        this.queries = queries;
        for (int[] crsPre: prerequisites) {
            if (!adj.containsKey(crsPre[1])) {
                adj.put(crsPre[1], new HashSet<>());
            }
            adj.get(crsPre[1]).add(crsPre[0]);
        }
        
        for (int i = 0; i < numCourses; i++) {
            dfs(i);
        }

        for (int[] q: queries) {
            res.add(graph.containsKey(q[1]) && graph.get(q[1]).contains(q[0]));
        }
        
        return res;
    }

    public Set<Integer> dfs(int crs) {
        Set<Integer> reachable = new HashSet<>();
        if (!adj.containsKey(crs)) {
            return reachable;
        }
        if (graph.containsKey(crs)){
            return graph.get(crs);
        }

        for (int nei: adj.get(crs)) {
            reachable.add(nei);
            reachable.addAll(dfs(nei));
        }
        graph.put(crs, reachable);
        return reachable;
    }
}