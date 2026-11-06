class Solution {
    Map<String, Map<String, Double>> adj;
    Map<String, Map<String, Double>> graph;

    public double[] calcEquation(
        List<List<String>> equations, double[] values, List<List<String>> queries) {
        adj = new HashMap<>();
        graph = new HashMap<>();

        for (int i = 0; i < equations.size(); i++) {
            String n1 = equations.get(i).get(0);
            String n2 = equations.get(i).get(1);
            double val = values[i];

            adj.computeIfAbsent(n1, k -> new HashMap<String, Double>()).put(n2, val);
            adj.computeIfAbsent(n2, k -> new HashMap<String, Double>()).put(n1, 1.0 / val);
        }

        for (String key: adj.keySet()) {
            graph.put(key, new HashMap<>());
            dfs(key, key, 1, new HashSet<>());
        }

        double[] res = new double[queries.size()];

        for (int i = 0; i < queries.size(); i++) {
            String n1 = queries.get(i).get(0);
            String n2 = queries.get(i).get(1);

            res[i] = graph.containsKey(n1) ? graph.get(n1).getOrDefault(n2, -1.0) : -1.0;
        }
        return res;
    }

    public void dfs(String prev, String n1, double ratio, Set<String> visited) {
        if (visited.contains(n1)) {
            return;
        }
        visited.add(n1);
        graph.get(prev).put(n1, ratio);


        for (Map.Entry<String, Double> entry: adj.get(n1).entrySet()) {
            String n2 = entry.getKey();
            double val = entry.getValue();
            dfs(prev, n2, ratio * val, visited); 
        }

    }
}