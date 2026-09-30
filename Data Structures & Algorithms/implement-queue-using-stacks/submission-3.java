class MyQueue {
    private Stack<Integer> st1;
    private Stack<Integer> st2;
    public MyQueue() {
        this.st1 = new Stack<>();
        this.st2 = new Stack<>();
    }

    public void push(int x) {
        this.st2.push(x);
    }

    public int pop() {
        if (this.st1.isEmpty()) {
            while (!this.st2.isEmpty()) {
                this.st1.push(this.st2.pop());
            }
        }
        return this.st1.pop();
    }

    public int peek() {
        if (this.st1.isEmpty()) {
            while (!this.st2.isEmpty()) {
                this.st1.push(this.st2.pop());
            }
        }
        return this.st1.peek();
    }

    public boolean empty() {
        return this.st1.isEmpty() && this.st2.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */