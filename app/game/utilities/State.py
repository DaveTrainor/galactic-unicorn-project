class State():
    def __init__(self, initial_state):
        self.state = initial_state
        self.initial = initial_state

    def set(self, new_state):
        self.state = new_state

    def get(self):
        return self.state

    def reset(self):
        self.state = self.initial
