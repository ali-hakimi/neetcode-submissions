class Solution {
    public int calPoints(String[] operations) {
        int res = 0;
        Stack<Integer> stack = new Stack<>();
        for (String op : operations) {
            if (op.equals("+")) {
                int v1 = stack.pop(), v2 = stack.pop();
                int sum = v1 + v2;
                res += sum;
                stack.push(v2);
                stack.push(v1);
                stack.push(sum);
            } else if (op.equals("D")) {
                int dbl = stack.peek() * 2;
                res += dbl;
                stack.push(dbl);
            } else if (op.equals("C")) {
                int invalid = stack.pop();
                res -= invalid;
            } else {
                int num = Integer.parseInt(op);
                stack.push(num);
                res += num;
            }
        }
        return res;
    }
}