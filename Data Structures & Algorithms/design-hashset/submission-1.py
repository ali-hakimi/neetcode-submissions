class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyHashSet:
    def __init__(self):
        self.n = 10000
        self.arr = [ListNode(0) for i in range(self.n)]

    def add(self, key: int) -> None:
        head = self.arr[key % self.n]
        while head.next:
            if head.next.val == key:
                return
            head = head.next
        head.next = ListNode(key)

    def remove(self, key: int) -> None:
        head = self.arr[key % self.n]
        while head.next:
            if head.next.val == key:
                head.next = head.next.next
                return
            head = head.next

    def contains(self, key: int) -> bool:
        head = self.arr[key % self.n]
        while head.next:
            if head.next.val == key:
                return True
            head = head.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
