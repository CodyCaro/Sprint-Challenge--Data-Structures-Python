class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        self.data.append(item)

        if len(self.data) == self.capacity:
            self.cur = 0
        elif len(self.data) > self.capacity:
            self.data[self.cur] = item
            print(self.data[self.cur])
            self.cur = (self.cur + 1) % self.capacity
            self.data.pop()

    def get(self):
        return self.data
