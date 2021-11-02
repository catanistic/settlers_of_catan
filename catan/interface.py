class GameInterface():
    def __init__(self):
        pass

    def attachObserver(self, observer):
        pass

    def detachObserver(self, observer):
        pass

    @property
    def action_space(self):
        pass

    def step(self, action):
        pass

    def observation(self):
        pass