class GameInterface():
    def __init__(self):
        pass

    def setUp(self):
        pass

    def addActor(self, actor_name=None):
        pass

    def attachObserver(self, observer):
        pass

    def detachObserver(self, observer):
        pass

    def reset(self):
        pass

    @property
    def action_space(self):
        pass

    def step(self, action):
        pass

    @property
    def observation(self):
        pass