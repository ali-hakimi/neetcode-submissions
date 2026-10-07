class Node {
    String word;
    Map<Character, Node> children;

    public Node() {
        this.children = new HashMap<>();
    }
}
class PrefixTree {
    Node root;
    public PrefixTree() {
        this.root = new Node();
    }

    public void insert(String word) {
        Node cur = this.root;

        for (char c : word.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                cur.children.put(c, new Node());
            }
            cur = cur.children.get(c);
        }
        cur.word = word;
    }

    public boolean search(String word) {
        Node cur = this.root;
        for (char c : word.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                return false;
            }
            cur = cur.children.get(c);
        }
        return cur.word != null;
    }

    public boolean startsWith(String prefix) {
        Node cur = this.root;
        for (char c : prefix.toCharArray()) {
            if (!cur.children.containsKey(c)) {
                return false;
            }
            cur = cur.children.get(c);
        }
        return true;
    }
}
