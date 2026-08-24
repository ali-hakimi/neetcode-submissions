class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next= next
class MyHashMap:

    def __init__(self):
        self.n = 10000
        self.arr = [ListNode() for i in range(self.n)]
        
    def put(self, key: int, value: int) -> None:
        head = self.arr[key % self.n]
        while head.next:
            if head.next.key == key:
                head.next.val = value
                return
            head = head.next
        head.next = ListNode(key, value)

    def get(self, key: int) -> int:
        head = self.arr[key% self.n]
        while head.next:
            if head.next.key == key:
                return head.next.val
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        head = self.arr[key%self.n]
        while head.next:
            if head.next.key == key:
                head.next = head.next.next
                return
            head = head.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)