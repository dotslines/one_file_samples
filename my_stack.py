"""--STACK model--"""


class Item:
    """
    An element model.
    Attributes:
        data(any type),
        next_item(pushed into the stack right before this item).
    """
    def __init__(self, data):
        self.data = data
        self.next_item = None


class MyStack:
    """
    A stack model class.
    Methods: push, pop, peak.
    (LIFO)
    """
    def __init__(self):
        """
        initiates the stack
        """
        self.size = 0
        self.current_item = None

    def push_item(self, data):
        """
        adds item into the stack
        """
        n_item = self.current_item
        self.current_item = Item(data=data)
        self.current_item.next_item = n_item
        self.size += 1

    def pop_item(self):
        """
        removes current(last pushed) item
        and returns its data
        """
        if self.size:
            c_item = self.current_item.next_item
            data = self.current_item.data
            del self.current_item
            self.size -= 1
            self.current_item = c_item
            return data
        else:
            print('There is no item to pop, the stack is empty.')

    def peak(self):
        """
        returns current(last pushed) items data
        """
        if self.size:
            return self.current_item.data
        else:
            print('There is no item to peak, the stack is empty.')
