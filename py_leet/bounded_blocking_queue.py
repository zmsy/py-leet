import threading
from typing import List


class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        """
        Blocked until space = semaphore used to gate values exist
        Blocked until empty = semaphore used to gate values do not exist
        """
        self.capacity = capacity
        self.mutex = threading.Lock()
        self.values = threading.Semaphore(capacity)
        self.empty = threading.Semaphore(0)
        self.queue: List[int] = []

    def enqueue(self, element: int) -> None:
        # wait until there are spaces available
        self.values.acquire()
        # wait until we've got exclusive access to the queue
        with self.mutex:
            self.queue.append(element)
            self.empty.release()

    def dequeue(self) -> int:
        self.empty.acquire()
        val = None
        with self.mutex:
            val = self.queue.pop(0)
            self.values.release()
        return val

    def size(self) -> int:
        with self.mutex:
            return len(self.queue)
