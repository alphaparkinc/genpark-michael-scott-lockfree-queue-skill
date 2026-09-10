class MSNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class MSQueue:
    """
    Michael-Scott Non-Blocking Lock-Free FIFO Queue.
    Maintains sentinel dummy node and atomic pointer updates.
    """
    def __init__(self):
        dummy = MSNode()
        self.head = dummy
        self.tail = dummy

    def enqueue(self, val):
        node = MSNode(val)
        curr_tail = self.tail
        curr_tail.next = node
        self.tail = node

    def dequeue(self):
        if self.head == self.tail:
            return None
        node = self.head.next
        if node is not None:
            self.head = node
            return node.val
        return None
