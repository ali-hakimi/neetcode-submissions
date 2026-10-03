/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;


    public Node() {
        this.val = false;
        this.isLeaf = false;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }

    public Node(boolean val, boolean isLeaf) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }

    public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node
bottomRight) { this.val = val; this.isLeaf = isLeaf; this.topLeft = topLeft; this.topRight =
topRight; this.bottomLeft = bottomLeft; this.bottomRight = bottomRight;
    }
}
*/

class Solution {
    private int[][] grid;
    public Node construct(int[][] grid) {
        this.grid = grid;

        return construct(0, 0, grid.length, grid.length);
    }

    private Node construct(int r1, int c1, int r2, int c2) {
        Node node = new Node();

        boolean isUnanimous = true;
        for (int i = r1; i < r2; i++) {
            for (int j = c1; j < c2; j++) {
                if (grid[i][j] != grid[r1][c1]) {
                    isUnanimous = false;
                    break;
                }
            }
        }
        if (isUnanimous) {
            node.isLeaf = true;
            node.val = grid[r1][c1] == 1;
            return node;
        }

        int rMid = (r1 + r2) / 2;
        int cMid = (c1 + c2) / 2;
        node.topLeft = construct(r1, c1, rMid, cMid);
        node.topRight = construct(r1, cMid, rMid, c2);
        node.bottomLeft = construct(rMid, c1, r2, cMid);
        node.bottomRight = construct(rMid, cMid, r2, c2);
        return node;
    }
}