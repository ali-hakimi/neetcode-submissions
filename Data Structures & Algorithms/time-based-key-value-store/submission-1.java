class TimeMap {
    public static class Pair<K, V> {
        private final K key;
        private final V val;

        public Pair(K key, V val) {
            this.key = key;
            this.val = val;
        }

        public K getKey() {
            return this.key;
        }
        public V getVal() {
            return this.val;
        }
    }

    private Map<String, List<Pair<Integer, String>>> keyStore;

    public TimeMap() {
        keyStore = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        keyStore.computeIfAbsent(key, k -> new ArrayList<>()).add(new Pair(timestamp, value));
    }
    
    public String get(String key, int timestamp) {
        List<Pair<Integer, String>> values = this.keyStore.getOrDefault(key, new ArrayList<>());
        int l = 0, r = values.size() - 1;
        String res = "";
        while (l <= r) {
            int m = l + (r- l) / 2;
            Pair mid = values.get(m);
            if ((int) mid.key == timestamp) {
                return (String) mid.val;
            }
            if ((int) mid.key < timestamp) {
                res = (String) mid.val;
                l = m + 1;
            }
            else {
                r = m - 1;
            }
        }
        return res;
    }
}
