class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
    
    def increment(self):
        self.counter += 1

    def reset(self):
        self.counter = 0

    def check_limit(self):
        if self.counter >= self.limit:
            self.reset()
            return True
