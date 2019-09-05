"""QUEUE model"""


class Item:
    """
    An element model.
    Attributes:
        data(any type),
        previous_item(pushed into the queue right after this item).
    """
    def __init__(self, data):
        self.data = data
        self.previous_item = None


class MyQueue:
    """
    A queue model class.
    Methods: push, pop, peak.
    (FIFO)
    """
    def __init__(self):
        """
        initiates the queue
        """
        self.size = 0
        self.current_item = None

    def push_item(self, data):
        """
        adds item into the queue
        """
        if self.current_item:
            self.current_item.previous_item = Item(data=data)
        else:
            self.current_item = Item(data=data)
        self.size += 1

    def pop_item(self):
        """
        removes current(first pushed) item
        and returns its data
        """
        if self.size:
            c_item = self.current_item.previous_item
            data = self.current_item.data
            del self.current_item
            self.size -= 1
            self.current_item = c_item
            return data
        else:
            print('There is no item to pop, the queue is empty.')

    def peak(self):
        """
        returns current(first pushed) item's data
        """
        if self.size:
            return self.current_item.data
        else:
            print('There is no item to peak, the queue is empty.')
