class Node {
    int key;
    int val;
    Node prev;
    Node next;
    public Node(int key, int val) {
        this.key = key;
        this.val = val;
    }
}

class LRUCache {
    private int cap;
    private Node left, right;
    private Map<Integer, Node> cache;

    public LRUCache(int capacity) {
        this.cap = capacity;
        this.left = new Node(0,0);
        this.right = new Node(0,0);
        this.left.next = this.right;
        this.right.prev = this.left;
        this.cache = new HashMap<>();
    }

    private void insert(Node node) {
        Node prev = right.prev;
        prev.next = node;
        node.prev = prev;
        node.next = right;
        right.prev = node;
    }

    private void remove(Node node) {
        Node prev = node.prev;
        Node next = node.next;
        prev.next = next;
        next.prev = prev;
    }
    
    public int get(int key) {
        if (!this.cache.containsKey(key)) {
            return -1;
        }
        Node node = this.cache.get(key);
        remove(node);
        insert(node);
        return node.val;        
    }
    
    public void put(int key, int value) {
        if (this.cache.containsKey(key)) {
            remove(this.cache.get(key));
        }

        this.cache.put(key, new Node(key, value));
        insert(this.cache.get(key));
        if (this.cache.size() > this.cap) {
            Node leastUsed = this.left.next;
            remove(leastUsed);
            this.cache.remove(leastUsed.key);
        }
    }
}
