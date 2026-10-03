class Solution {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> map = new HashMap<>();
        for (char t : tasks) {
            map.put(t, map.getOrDefault(t, 0) + 1);
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int val : map.values()) {
            pq.offer(val);
        }

        PriorityQueue<int[]> coolDown = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        int time = 0;
        while (!pq.isEmpty() || !coolDown.isEmpty()) {
            if (!pq.isEmpty()) {
                int taskCount = pq.poll();
                taskCount--;
                if (taskCount > 0) {
                    coolDown.offer(new int[] {time + n, taskCount});
                }
            }
            while (!coolDown.isEmpty() && coolDown.peek()[0] <= time) {
                int[] task = coolDown.poll();
                pq.offer(task[1]);
            }
            time++;
        }

        return time;
    }
}
