class Node:
    def __init__(self, val=0, next=None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.l = Node()
        self.r = Node()
        self.l.next = self.r
        self.r.prev = self.l

    def insertFront(self, value: int) -> bool:
        if self.size + 1 > self.k:
            return False
        prev = self.r.prev
        newNode = Node(value, self.r, prev)
        prev.next = newNode
        self.r.prev = newNode
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size + 1 > self.k:
            return False
        nextNode = self.l.next
        newNode = Node(value, nextNode, self.l)
        nextNode.prev = newNode
        self.l.next = newNode
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        front = self.getFront()
        if front == -1:
            return False
        front = self.r.prev
        prev = front.prev
        prev.next = self.r
        self.r.prev = prev
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        rear = self.getRear()
        if rear == -1:
            return False
        rear = self.l.next
        nextNode = rear.next
        nextNode.prev = self.l
        self.l.next = nextNode
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.r.prev.val if self.r.prev != self.l else -1

    def getRear(self) -> int:
        return self.l.next.val if self.l.next != self.r else -1
        

    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size == self.k

        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()